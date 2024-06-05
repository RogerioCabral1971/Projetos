import requests
import pandas as pd
import streamlit as st
import situacoes as sit
import canal_venda as cv
import xmltodict

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization':f"{st.secrets['db_credentials']['token']}",
  'Cookie': f"{st.secrets['db_credentials']['Cookie']}"
}
def nota_fiscal(url):
    cont=0
    df = pd.DataFrame()
    while True:
        cont = cont + 1
        nf = url + str(cont)
        response_nf = requests.request("GET", nf, headers=headers, data=payload)
        df_nf=pd.DataFrame(response_nf.json()['data'])
        if len(df_nf) > 0:
            df_nf = cv.canal_venda(df_nf)
            #df_nf = sit.situacao(df_nf)
            df = pd.concat([df, df_nf])
        else:
            break
    return df


def arqXml_valor_importo(id):
    try:
        url = f"https://bling.com.br/Api/v3/pedidos/vendas/{id}"
        response_vendas = requests.request("GET", url, headers=headers, data=payload)
        id_nf=response_vendas.json()['data']['notaFiscal']['id']
        url = f"https://bling.com.br/Api/v3/nfe/{id_nf}"
        response_nf = requests.request("GET", url, headers=headers, data=payload)
        sitexml = response_nf.json()['data']['xml']
        url = sitexml
        response_xml = requests.request("GET", url, headers=headers, data=payload)
        arqXml = response_xml.text
        df = xmltodict.parse(arqXml)
        valor_total_tributo=df['nfeProc']['NFe']['infNFe']['det']['imposto']['vTotTrib']
    except:
        valor_total_tributo=0

    return valor_total_tributo