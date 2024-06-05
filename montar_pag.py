import streamlit as st
import relatorio_plenoled as rel

def formatar_num(valor):
    valor_frmt="{:,.2f}".format(valor).replace(',','_').replace('.',',').replace('_','.')
    return valor_frmt


def cartao_resumo(df):
    colunas = ['col1', 'col2', 'col3', 'col4']
    colunas = st.columns(4)
    colunas[0].metric(f"TOTAL VENDA BRUTA - {df['Quantidade Venda'].sum()} Vendas", formatar_num(df['Total R$'].sum().round(0)))
    colunas[0].text(f"TOTAL IMPOSTO R$ {formatar_num(df['Valor Imposto'].sum())}")
    colunas[0].text(f"Venda Líquida R$ {formatar_num(df['Total R$'].sum()-df['Valor Imposto'].sum())}")
    for idx in df['Canal de Venda'].index:
        colunas[idx+1].metric(f"{str(df['Canal de Venda'][idx]).upper()} - {df['Quantidade Venda'][idx]} Vendas", formatar_num(df['Total R$'][idx]))
        colunas[idx + 1].text(f"Imposto R$ {formatar_num(df['Valor Imposto'][idx])}")
        colunas[idx + 1].text(f"Venda Líquida R$ {formatar_num(df['Total R$'][idx]-df['Valor Imposto'][idx])}")

def tabela_resumo(df,inicial,fim):
    df=st.data_editor(df,key='tabresumo')
    st.data_editor(rel.resumo_nf(inicial,fim))