import pandas as pd
import canal_venda as cv
import situacoes as st
import requests


payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 7fe30c52d2b20d4e1488d0188c90e331f45a9f49',
  'Cookie': 'PHPSESSID=15de1ths4uag634bfr9fcqhivm'
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
      df_vendas = st.situacao(df_vendas)
      df = pd.concat([df, df_vendas])
    else:
      break

  return df

