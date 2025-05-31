Hier ist eine detaillierte **README.md**-Datei für deine Streamlit-App (`app.py`). Sie enthält eine vollständige Beschreibung des Projekts, Installationsanweisungen und eine Anleitung zur Nutzung des Dashboards. 🚀  

---

### **📌 README.md für dein Krypto-Live-Dashboard**
```markdown
# 📈 Krypto Live-Dashboard mit Streamlit  

Dies ist ein **Streamlit-Dashboard**, das die aktuellen Krypto-Preise aus einer **PostgreSQL-Datenbank** lädt und **grafisch darstellt**. Die Daten werden von **CoinMarketCap** über Web Scraping extrahiert und in die Datenbank gespeichert.  

---

## 🔍 **Projektübersicht**  
**Was macht dieses Dashboard?**  
✅ **Lädt Echtzeit-Krypto-Preise aus PostgreSQL** für Analysen.  
✅ **Visualisiert Preisentwicklungen mit interaktiven Diagrammen**.  
✅ **Ermöglicht die Auswahl verschiedener Kryptowährungen** für detaillierte Analysen.  
✅ **Live-Daten ohne API-Abhängigkeit**, da die Datenbank regelmäßig aktualisiert wird.  

---

## ⚡ **Installation & Vorbereitung**  
### 1️⃣ **Erforderliche Bibliotheken installieren**  
Falls du die notwendigen Bibliotheken noch nicht installiert hast, führe diesen Befehl aus:  
```bash
pip install streamlit psycopg2 pandas sqlalchemy
```

### 2️⃣ **PostgreSQL-Datenbank einrichten**  
Falls du noch keine Datenbank hast, erstelle sie mit:
```sql
CREATE DATABASE crypto_db;
```
Falls die Tabelle nicht existiert, erstelle sie mit:
```sql
CREATE TABLE crypto_prices (
    id SERIAL PRIMARY KEY,
    utcdate TIMESTAMP DEFAULT NOW(),
    coin VARCHAR(50),
    price FLOAT
);
```

Falls du Daten testen möchtest, füge sie manuell hinzu:
```sql
INSERT INTO crypto_prices (utcdate, coin, price) VALUES (NOW(), 'Bitcoin', 50000.00);
INSERT INTO crypto_prices (utcdate, coin, price) VALUES (NOW(), 'Ethereum', 3500.00);
```

### 3️⃣ **Starten des Dashboards**  
Speichere den Code als `app.py` und starte die Streamlit-App mit:
```bash
streamlit run app.py
```

---

## 🔄 **Funktionsweise des Dashboards**  
### 📌 **Hauptfunktionen**  
✅ **Lädt aktuelle Krypto-Daten aus PostgreSQL**  
✅ **Ermöglicht die Filterung nach Kryptowährung**  
✅ **Zeigt Preisverläufe in Echtzeit**  

### 📌 **Wie die Daten geladen werden**  
1️⃣ **Die App verbindet sich mit PostgreSQL** und ruft die letzten 50 Datensätze ab:  
```sql
SELECT * FROM crypto_prices ORDER BY utcdate DESC LIMIT 50;
```
2️⃣ **Die Daten werden als Pandas-DataFrame geladen** und in Streamlit dargestellt.  
3️⃣ **Die Preisentwicklung wird mit `st.line_chart()` grafisch angezeigt**.  

---

## 📌 **Codeübersicht für `app.py`**
Falls du den **kompletten Code** benötigst, hier eine kurze Übersicht:

```python
import streamlit as st
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# PostgreSQL-Verbindungsdetails
DB_USER = "your_user"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "crypto_db"

# Verbindung zur Datenbank
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Funktion zum Laden der Daten
@st.cache_data
def get_data():
    query = "SELECT * FROM crypto_prices ORDER BY utcdate DESC LIMIT 50;"
    df = pd.read_sql(query, engine)
    return df

df = get_data()

# Streamlit Dashboard
st.set_page_config(page_title="Krypto Live-Dashboard", layout="wide")
st.title("📈 Live-Krypto-Dashboard")
st.dataframe(df, width=1000, height=500)

# Auswahl der Kryptowährung
coin_options = df["coin"].unique()
coin = st.selectbox("Wähle eine Kryptowährung:", coin_options)

# Preisverlauf anzeigen
filtered_df = df[df["coin"] == coin]
st.subheader("📊 Preisverlauf")
st.line_chart(filtered_df.set_index("utcdate")["price"])
```

---

## 🔎 **Fehlersuche & Debugging**  
Falls du **keine Daten im Dashboard siehst**, überprüfe deine PostgreSQL-Datenbank mit:  
```sql
SELECT COUNT(*) FROM crypto_prices;
```

Falls **keine Tabelle existiert**, erstelle sie manuell mit:
```sql
CREATE TABLE crypto_prices (
    id SERIAL PRIMARY KEY,
    utcdate TIMESTAMP DEFAULT NOW(),
    coin VARCHAR(50),
    price FLOAT
);
```

Falls **keine Verbindung zur Datenbank** möglich ist, prüfe deine Zugangsdaten in `app.py`:
```python
DB_USER = "your_user"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "crypto_db"
```

Falls **Fehler beim Kodieren auftreten**, verwende:
```python
df = pd.read_sql(query, engine, encoding="utf-8")
```

---

## 📌 **Erweiterungsmöglichkeiten**  
Falls du dein Krypto-Dashboard erweitern möchtest, kannst du:  
✅ **Live-Updates mit `st.experimental_rerun()` hinzufügen**  
✅ **Mehrere Kryptowährungen gleichzeitig vergleichen**  
✅ **Trading-Signale basierend auf Preisverläufen generieren**  
✅ **Maschinelles Lernen für Preisprognosen einbauen**  

---

## 🎯 **Fazit**  
✅ **Streamlit-Dashboard für Echtzeit-Krypto-Daten**  
✅ **Einfache Installation & PostgreSQL-Anbindung**  
✅ **Interaktive Preisgrafiken & Filtermöglichkeiten**  
✅ **Leicht erweiterbar mit neuen Funktionen**  
```

---

### **📌 Fazit**
✅ **Diese README.md bietet eine klare Anleitung für dein Streamlit-Dashboard**  
✅ **Enthält Installationsanweisungen, Fehlerbehebung und Code-Übersicht**  
✅ **Ideal für Dokumentation, Debugging und zukünftige Verbesserungen**  

Hier ist eine gut strukturierte **README.md**-Datei für deine `script.py`. Sie enthält eine detaillierte Übersicht über das Projekt, einschließlich der wichtigsten Korrekturen, Installationsanweisungen und Funktionsbeschreibung. 🚀  

---

### **📌 README.md für dein Krypto-ETL-Projekt**
```markdown
# 📊 Krypto-ETL-Pipeline mit Web Scraping & PostgreSQL  

Dies ist eine **ETL-Pipeline**, die aktuelle Krypto-Preise von **CoinMarketCap** per **Web Scraping** extrahiert und in einer **PostgreSQL-Datenbank** speichert. 🚀  

---

## 🔍 **Projektübersicht**  
**Was macht dieses Skript?**  
✅ **Web Scraping mit Selenium & BeautifulSoup** für aktuelle Krypto-Preise.  
✅ **Speicherung der Daten in PostgreSQL** für langfristige Analysen.  
✅ **Automatische Tabellen- und Spaltenprüfung**, um Datenbankfehler zu vermeiden.  
✅ **Streamlit-Dashboard für Live-Preisvisualisierung**.  

---

## ⚡ **Installation & Vorbereitung**  
### 1️⃣ **Erforderliche Bibliotheken installieren**  
Führe diesen Befehl aus, um alle notwendigen Bibliotheken zu installieren:  
```bash
pip install selenium webdriver-manager psycopg2 pandas sqlalchemy streamlit
```

### 2️⃣ **PostgreSQL-Datenbank einrichten**  
Erstelle eine **PostgreSQL-Datenbank** mit folgendem SQL-Befehl:  
```sql
CREATE DATABASE crypto_db;
```
Falls du noch keine Tabelle hast, kannst du sie mit folgendem SQL-Code erstellen:  
```sql
CREATE TABLE crypto_prices (
    id SERIAL PRIMARY KEY,
    utcdate TIMESTAMP DEFAULT NOW(),
    coin VARCHAR(50),
    price FLOAT
);
```

### 3️⃣ **Starten des Skripts**  
Führe die ETL-Pipeline aus mit:
```bash
python minietl.py
```

### 4️⃣ **Starten des Dashboards**  
Falls du das **Live-Dashboard** mit Streamlit verwenden möchtest:
```bash
streamlit run minietl.py
```

---

## 🔄 **Workflow der ETL-Pipeline**  
1️⃣ **Extraktion**: Holt die neuesten Krypto-Preise von **CoinMarketCap** mittels **Selenium & BeautifulSoup**.  
2️⃣ **Transformation**: Konvertiert die Daten in ein **Pandas-DataFrame** und sichert die richtigen Spalten.  
3️⃣ **Laden**: Speichert die Krypto-Daten in **PostgreSQL** für spätere Analysen.  

---

## 🔧 **Wichtige Korrekturen & Verbesserungen**  
### 🔹 **Spaltenproblem mit `utcDate` behoben**  
✅ PostgreSQL speichert die Zeitstempel in der Spalte `utcdate` statt `utcDate`.  
✅ Automatische Umbenennung `utcDate` → `utcdate` vor dem Speichern.  

### 🔹 **Web Scraping verbessert**  
✅ Verwendung von **Selenium statt `requests`**, um JavaScript-generierte Inhalte korrekt zu scrapen.  
✅ **User-Agent hinzugefügt**, um Scraping-Blockaden zu umgehen.  
✅ **Aktualisierte Selektoren**, um Coins und Preise zuverlässig zu extrahieren.  

### 🔹 **Datenbank-Fehlertoleranz erhöht**  
✅ **Automatische Tabellenprüfung**, bevor neue Daten gespeichert werden.  
✅ Falls `crypto_prices` fehlt, wird sie **automatisch erstellt**.  
✅ Falls `utcdate` nicht vorhanden ist, wird sie **automatisch hinzugefügt**.  

### 🔹 **Optimierung für Streamlit-Dashboard**  
✅ **Live-Preisverläufe mit interaktiven Charts**.  
✅ **Filterbare Tabellenansicht**, um spezifische Coins auszuwählen.  

---

## 📌 **Zusätzliche Features & Erweiterungen**  
Falls du dein Projekt erweitern möchtest, kannst du:  
✅ **Historische Preisanalysen hinzufügen**  
✅ **Machine Learning für Preisprognosen einbinden**  
✅ **Trading-Signale basierend auf Preisbewegungen entwickeln**  
✅ **API-Anbindung für Echtzeit-Daten erweitern**  

---

## 🔎 **Fehlersuche & Debugging**  
Falls du Probleme hast, prüfe folgende SQL-Befehle zur Fehleranalyse:  

🔹 **Existiert die Tabelle?**  
```sql
SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';
```

🔹 **Welche Spalten sind verfügbar?**  
```sql
SELECT column_name FROM information_schema.columns WHERE table_name = 'crypto_prices';
```

🔹 **Gibt es gespeicherte Einträge?**  
```sql
SELECT COUNT(*) FROM crypto_prices;
```

```

---

### **📌 Fazit**
✅ **Diese README-Datei bietet alle wichtigen Informationen für dein Projekt.**  
✅ **Enthält Installationsanweisungen, Fehlerbehebung und Erweiterungsmöglichkeiten.**  
✅ **Ideal für Dokumentation, Debugging und zukünftige Verbesserungen!**  
