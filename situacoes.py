import pandas as pd
import time
import extrair_informacoes as extr
import streamlit as st
dir=st.secrets['pastas']['dir']

def situacao(df_vendas):
    df_situacoes_local = pd.read_parquet(f'{dir}situacoes.parquet')
    situacao = "https://bling.com.br/Api/v3/situacoes/"
    id_situacao=[]
    for id in df_vendas['situacao'].index:
      id_situacao.append(df_vendas['situacao'][id]['id'])
    df_vendas['id_situacao']=id_situacao
    desc_situacao=[]
    id_situacao_=df_vendas['id_situacao'].unique()
    for id2 in id_situacao_:
        desc=list(df_situacoes_local.query(f'id_situacao=={id2}')['Descr_situacao'])
        if len(desc)>0:
            desc = list(df_situacoes_local.query(f'id_situacao=={id2}')['Descr_situacao'])[0]
            desc_situacao.append(desc)
        else:
            temp_situacao = extr.extrai(situacao + str(id2))
            desc=pd.DataFrame([temp_situacao.json()['data']])['nome'][0]
            desc_situacao.append(desc)
            time.sleep(0.5)

    df_situacoes=pd.DataFrame(data={'id_situacao':id_situacao_,'Descr_situacao':desc_situacao})
    df_total=pd.merge(df_vendas,df_situacoes, on='id_situacao')
    return df_total