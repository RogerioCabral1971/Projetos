import requests
import pandas as pd
import time
import streamlit as st

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': st.secrets.db_credentials.token,
  'Cookie': st.secrets.db_credentials.Cookie
}

def situacao(df_vendas):
    situacao = "https://bling.com.br/Api/v3/situacoes/"
    id_situacao=[]
    for id in df_vendas['situacao'].index:
      id_situacao.append(df_vendas['situacao'][id]['id'])
    df_vendas['id_situacao']=id_situacao
    desc_situacao=[]
    id_situacao_=df_vendas['id_situacao'].unique()
    for id2 in id_situacao_:
      temp_situacao = requests.request("GET", situacao + str(id2), headers=headers, data=payload)
      desc=pd.DataFrame([temp_situacao.json()['data']])['nome'][0]
      desc_situacao.append(desc)
      time.sleep(0.5)
    df_situacoes=pd.DataFrame(data={'id_situacao':id_situacao_,'Descr_situacao':desc_situacao})
    df_total=pd.merge(df_vendas,df_situacoes, on='id_situacao')
    return df_total
