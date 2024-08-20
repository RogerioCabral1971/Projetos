import os
import datetime
import locale
import streamlit as st
import pandas as pd
import montar_pag as pag
import atualizar_bases
import extrair_informacoes as ext
import relatorio_plenoled as rel
import baixar_atualização
import abrirArq

# CONFIGURAÇÃO DA PAGINA
st.set_page_config(layout='wide', page_title='PlenoLed',initial_sidebar_state='collapsed')


today=datetime.date.today()
dt_inicio=today-datetime.timedelta(90)
dia=datetime.timedelta(1)
dire=ext.ler_toml()['pastas']['dir']

