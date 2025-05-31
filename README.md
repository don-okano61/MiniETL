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
