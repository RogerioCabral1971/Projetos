import streamlit as st
import pandas as pd

arq=st.file_uploader("Escolho",accept_multiple_files=True)
st.write(pd.read_parquet(arq[0]))



