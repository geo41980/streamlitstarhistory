import streamlit as st
import pandas as pd

# Sheets-URL aus den Geheimnissen lesen
sheets_url = st.secrets["public_gsheets_url"]

st.write("Hallo Georg")
# Daten aus der Google Sheet abrufen
#df = pd.read_csv(sheets_url)

# Daten in Streamlit anzeigen
#st.dataframe(df)
