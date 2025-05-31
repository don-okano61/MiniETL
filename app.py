import streamlit as st
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# PostgreSQL-Verbindungsdetails
DB_USER = ""                    #Benutzername
DB_PASSWORD = ""                #Passwort
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "crypto_db"

# Verbindung zur PostgreSQL-Datenbank
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Streamlit App
st.set_page_config(page_title="Krypto Live-Dashboard", layout="wide")

st.title("📈 Live-Krypto-Dashboard")
st.write("Hier siehst du die aktuellen Krypto-Preise aus der Datenbank.")

# Funktion zum Laden der Daten aus PostgreSQL
@st.cache_data
def get_data():
    query = "SELECT * FROM crypto_prices ORDER BY utcdate DESC LIMIT 50;"
    df = pd.read_sql(query, engine)
    return df

df = get_data()

# Anzeigen der Daten
st.dataframe(df, width=1000, height=500)

# Visualisierung der Preisentwicklung
st.subheader("📊 Preisverlauf der Kryptowährungen")

# Auswahl der Kryptowährung
coin_options = df["coin"].unique()
coin = st.selectbox("Wähle eine Kryptowährung:", coin_options)

# Filtere die Daten
filtered_df = df[df["coin"] == coin]

# Linie-Diagramm für Preisentwicklung
st.line_chart(filtered_df.set_index("utcdate")["price"])

st.write("🔄 Die Daten werden direkt aus der PostgreSQL-Datenbank geladen!")