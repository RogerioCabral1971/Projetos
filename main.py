import streamlit as st
import pandas as pd
import tomllib


arq=st.file_uploader("Escolho",accept_multiple_files=True)
st.write(tomllib.load(arq))





