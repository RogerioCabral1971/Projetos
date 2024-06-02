import pandas as pd
import canal_venda as cv
import situacoes as sit
import requests
import streamlit as st


payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': st.secrets.db_credentials.token,
  'Cookie': st.secrets.db_credentials.Cookie
}


def vendas(url):
  cont = 0
  df = pd.DataFrame()
  while True:
    cont=cont+1
    vendas = url+str(cont)
    response_vendas = requests.request("GET", vendas, headers=headers, data=payload)
    df_vendas=pd.DataFrame(response_vendas.json()['data'])
    if len(df_vendas)>0:
      df_vendas = cv.canal_venda(df_vendas)
      df_vendas = sit.situacao(df_vendas)
      df = pd.concat([df, df_vendas])
    else:
      break

  return df

