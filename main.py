import Relatorio
import datetime
import streamlit as st

today = datetime.datetime.now()
coluna_date1,coluna_date2,coluna_date3,coluna_date4=st.columns(4)
st.write(f"{st.secrets['db_credentials']['token']}")
inicial=coluna_date1.date_input('Data Inicio', datetime.date(2024,5,15),format='YYYY-MM-DD')
fim=coluna_date3.date_input('Data Final', today,format='YYYY-MM-DD')
st.data_editor(Relatorio.resumo_canal(inicial,fim, 'Finalizado'))








