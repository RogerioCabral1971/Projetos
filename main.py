import relatorio_plenoled as rel
import datetime
import streamlit as st
import pandas as pd
import montar_pag as pag
import atualizar_bases
today=datetime.date.today()
dia=datetime.timedelta(1)
status = 'Finalizado'
dir=st.secrets['pastas']['dir']

# CONFIGURAÇÃO DA PAGINA
st.set_page_config(layout='wide', page_title='PlenoLed', initial_sidebar_state="expanded")
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html=True)

# INFORMAÇÕES INICIAL DA PÁGINA
with st.container(border=True):
    col1,col2,col3,col4,col5,col6=st.columns([0.2,0.1,0.2,0.1,0.1,0.1])
    col1.image('img/plenoled.com.br.webp',width=250)
    periodo=col3.date_input('Selecione o Periodo', value=(pd.to_datetime('2024-05-31'), pd.to_datetime(f'{today}')))

# ATUALIZAÇÃO DA BASE DE DADOS
vendas=pd.read_parquet(f'{dir}pedidos_venda.parquet')
dt_inicial=pd.to_datetime(vendas['data'].max())
atualizado=pd.to_datetime(today)==dt_inicial


if atualizado==False:
    atualizar_bases.vendas(vendas, format(dt_inicial,'%Y-%m-%d'))
else:
    st.sidebar.success('Vendas OK')

atualizar_bases.valida_dados(vendas)

# GERAÇÃO DOS RELATÓRIOS
if col3.button('Gerar Relatório'):
    aba1, aba2 = st.tabs(['Resumo Canal de Venda', 'Resumo por Mercadoria'])
    inicial=periodo[0]
    fim=periodo[1]
    df=rel.resumo_canal(inicial,fim, status)
    if len(df[0])>0:
        with aba1:
            st.markdown(f"Resumo do Período de {inicial} até {fim}")
            pag.cartao_resumo(df[0])
        with aba2:
            pag.tabela_produto(df[1],df[2])
    else:
        st.warning('Data sem Movimentação')












