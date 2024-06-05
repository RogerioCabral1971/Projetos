import relatorio
import datetime
import streamlit as st
import pandas as pd
import montar_pag as pag
import plotly.express as px


st.set_page_config(layout='wide', page_title='PlenoLed', initial_sidebar_state="expanded")

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html=True)
today = datetime.datetime.now()

with st.container(border=True):
    col1,col2,col3,col4,col5,col6=st.columns([0.2,0.2,0.1,0.1,0.1,0.1])
    col1.image('img/plenoled.com.br.webp',width=250)
    periodo=col2.date_input('Selecione o Periodo', value=(pd.to_datetime('2024-05-31'), pd.to_datetime(f'{today}')))

if col2.button('Gerar Relatório'):
    inicial=periodo[0]
    fim=periodo[1]
    st.markdown(f"Resumo do Período de {inicial} até {fim}")
    df=Relatorio.resumo_canal(inicial,fim, 'Finalizado')
    pag.cartao_resumo(df)













