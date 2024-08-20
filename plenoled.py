import os
import datetime
import locale
import streamlit as st
import pandas as pd


# CONFIGURAÇÃO DA PAGINA
st.set_page_config(layout='wide', page_title='PlenoLed',initial_sidebar_state='collapsed')


today=datetime.date.today()
dt_inicio=today-datetime.timedelta(90)
dia=datetime.timedelta(1)
st.write(dt_inicio)


