import streamlit as st
import pandas as pd
import tomllib


arq=st.file_uploader("Escolho",accept_multiple_files=True)
st.write(arq[0])
st.write(tomllib.load(arq[0]))





