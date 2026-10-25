import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Apuração 2026 · Dashboard Interativo",
    page_icon="🗳️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .block-container { padding: 0rem !important; max-width: 100% !important; }
    header[data-testid="stHeader"], footer { display: none !important; }
    body { margin: 0; background-color: #0f1318; }
</style>
""", unsafe_allow_html=True)

# Lê o arquivo HTML externo sem risco de conflito de aspas no Python
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

components.html(html_data, height=2300, scrolling=True)
