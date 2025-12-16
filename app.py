import streamlit as st
from pathlib import Path

st.set_page_config(page_title="喜欢你", layout="centered")

html = Path("index.html").read_text()

st.markdown("# 喜欢你")
st.components.v1.html(html, height=720, scrolling=True)
