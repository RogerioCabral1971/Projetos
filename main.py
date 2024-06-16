import relatorio_plenoled as rel
import datetime
import streamlit as st
import pandas as pd
import montar_pag as pag
import atualizar_bases
import extrair_informacoes as ext
import tomllib
import requests

today=datetime.date.today()
dia=datetime.timedelta(1)
status = 'Finalizado'
dir=ext.ler_toml()['pastas']['dir']

# define the relative path of the sample file
file_path = "C:/PlenoLed/secrets.toml"

# store the target API URL
target_url = "https://httpbin.org/post"

# create a reference to the file
target_file = open(file_path, "rb")

# send the request
response = requests.post(target_url, files = {"form_field_name": target_file})

# check the result
if response.ok:
    st.write("Upload complete")
    st.write(response.text)
else:
    st.write("Something went wrong")







