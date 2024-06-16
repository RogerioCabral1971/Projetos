import streamlit as st

arq=st.file_uploader("Escolho",accept_multiple_files=True)
st.write(pd.read_parquet(arq[0]))



