import streamlit as st
import pandas as pd
from streamlit_file_browser import st_file_browser

arq=st.file_uploader("Escolho",accept_multiple_files=True)
st.write(pd.read_parquet(arq[0]))


st.header('Show only molecule files')
event = st_file_browser("example_artifacts", artifacts_site="http://localhost:1024", show_choose_file=True, show_download_file=False, glob_patterns=('molecule/*',), key='C')
st.write(event)



