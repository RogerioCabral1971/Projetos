import Relatorio
import datetime
import streamlit as st

today = datetime.datetime.now()
coluna_date1,coluna_date2,coluna_date3,coluna_date4=st.columns(4)

inicial=coluna_date1.date_input('Data Inicio', datetime.date(2024,5,1),format='YYYY-MM-DD')
fim=coluna_date3.date_input('Data Final', today,format='YYYY-MM-DD')
st.data_editor(Relatorio.resumo_canal('2024-05-01','2024-05-15', 'Finalizado'))








