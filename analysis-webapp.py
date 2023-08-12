import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
 
# Breite der Streamlit-Seite anpassen
st.set_page_config(
    page_title="Pygwalker in Streamlit verwenden",
    layout="wide"
)
 
# Titel hinzufügen
st.title("Pygwalker in Streamlit verwenden")
 
# Daten importieren
df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")
 
# HTML mit Pygwalker generieren
pyg_html = pyg.walk(df, return_html=True)
 
# HTML in die Streamlit-Anwendung einbetten
components.html(pyg_html, height=1000, scrolling=True)
