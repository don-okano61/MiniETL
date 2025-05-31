import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from sqlalchemy import create_engine
import psycopg2
import prefect
from prefect import flow, task

# PostgreSQL-Verbindungsdetails
DB_USER = ""                #Benutzername
DB_PASSWORD = ""            #Passwort
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "crypto_db"

# CoinMarketCap-URL für Web Scraping
URL = "https://coinmarketcap.com/"

# Manuell gesetzter Chrome-Pfad (falls nötig)
CHROME_BINARY_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Verbindung zur PostgreSQL-Datenbank
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

@task
def create_database():
    """ Erstellt die Datenbank und Tabelle, falls sie nicht existieren """
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        cursor = conn.cursor()

        # Tabelle erstellen, falls sie nicht existiert
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS crypto_prices (
                id SERIAL PRIMARY KEY,
                utcdate TIMESTAMP DEFAULT NOW(),
                coin VARCHAR(50),
                price FLOAT
            );
        """)
        conn.commit()

        cursor.close()
        conn.close()
        print("✅ Datenbank und Tabelle sind korrekt eingerichtet!")

    except Exception as e:
        print(f"❌ Fehler bei der Datenbank/Tabelle-Erstellung: {e}")

@task
def extract():
    """ Web Scraping von CoinMarketCap für aktuelle Krypto-Preise mit Selenium """
    try:
        # ChromeDriver initialisieren
        options = Options()
        options.binary_location = CHROME_BINARY_PATH  # Manuell gesetzter Chrome-Pfad
        options.add_argument("--headless")  # Unsichtbarer Browser-Modus

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Webseite laden
        driver.get(URL)
        html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(html, "html.parser")

        rows = []
        for row in soup.select("table.cmc-table tbody tr")[:10]:  # Top 10 Coins
            coin_tag = row.select_one("td:nth-child(3) p")
            price_tag = row.select_one("td:nth-child(4) span")

            if coin_tag and price_tag:
                coin_name = coin_tag.text.strip()
                price = price_tag.text.replace("$", "").replace(",", "").strip()

                rows.append({
                    "utcdate": pd.to_datetime("now"),  # Korrekte Schreibweise
                    "coin": coin_name,
                    "price": float(price)
                })

        if rows:
            print("✅ Krypto-Daten erfolgreich extrahiert:", rows)
        else:
            print("⚠️ Keine Krypto-Daten gefunden. Überprüfe die Selektoren.")

        return rows

    except Exception as e:
        print(f"❌ Fehler beim Scraping: {e}")
        return []

@task
def transform(rows):
    """ Transformiert die gescrapten Krypto-Daten """
    if not rows:
        print("🚨 Warnung: Keine Daten zum Transformieren!")
        return pd.DataFrame()

    df = pd.DataFrame(rows)
    
    # Sicherstellen, dass `utcdate` korrekt existiert
    if "utcdate" not in df.columns:
        df["utcdate"] = pd.to_datetime("now")

    print("✅ Krypto-Daten transformiert:", df)
    return df

@task
def load(df):
    """ Speichert die Krypto-Daten in PostgreSQL """
    if df.empty:
        print("🚨 Warnung: Keine Daten zum Speichern vorhanden!")
        return

    # Automatische Umbenennung der Spalte für PostgreSQL
    df.rename(columns={"utcDate": "utcdate"}, inplace=True)

    try:
        df.to_sql("crypto_prices", engine, if_exists="append", index=False)
        print("📊 Krypto-Daten erfolgreich gespeichert!")

    except Exception as e:
        print(f"❌ Fehler beim Speichern der Daten: {e}")

@flow
def etl_pipeline():
    create_database()
    rows = extract()
    transformed_data = transform(rows)
    load(transformed_data)

# Starte die ETL-Pipeline
if __name__ == "__main__":
    etl_pipeline()