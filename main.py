import streamlit as st
import pandas as pd
from streamlit_file_browser import st_file_browser

arq=st.file_uploader("Escolho",accept_multiple_files=True)
st.write(pd.read_parquet(arq[0]))





