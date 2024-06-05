import pandas as pd
import canal_venda as cv
import situacoes as sit
import requests
import streamlit as st
import nf as nfe

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization':f"{st.secrets['db_credentials']['token']}",
  'Cookie': f"{st.secrets['db_credentials']['Cookie']}"
}


def vendas(url,status):
  cont = 0
  df = pd.DataFrame()
  my_bar = st.progress(0, text="progress_text")
  while True:
    cont=cont+1
    my_bar.progress(cont, text=f'Página Linda...: {cont}')
    vendas = url+str(cont)
    response_vendas = requests.request("GET", vendas, headers=headers, data=payload)
    df_vendas=pd.DataFrame(response_vendas.json()['data'])
    if len(df_vendas)>0:
      df_vendas = cv.canal_venda(df_vendas)
      df_vendas = sit.situacao(df_vendas)
      df_vendas = df_vendas.query(f'Descr_situacao=="{status}"')
      df = pd.concat([df, df_vendas])
    else:
      break
  df = df.reset_index()
  my_bar.empty()
  my_bar = st.progress(0, text="progress_text")
  for idx in df.index:
    my_bar.progress(cont, text=f'Imposto lindo...: {idx} de {len(df)}')
    try:
      id=df['id'][idx]
      valor_imposto=nfe.arqXml_valor_importo(id)
      df.loc[df['id']==id,"Valor Imposto"]=float(valor_imposto)

    except:
      pass
  my_bar.empty()
  return df

