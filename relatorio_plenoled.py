import pandas as pd
import vendas as vd
import nf as nf
import streamlit as st

def resumo_canal(dt_inicial,dt_fim, status_pedido):
    df=vd.vendas(f"https://bling.com.br/Api/v3/pedidos/vendas?dataInicial={dt_inicial}&dataFinal={dt_fim}&pagina=",status_pedido)

    df2=df.groupby('origem_venda').total.agg(['count','sum','mean']).rename(columns={
       'count':'Quantidade Venda','sum':'Total R$', 'mean':'Media R$'})
    df2.reset_index(inplace=True)
    df3 = df.groupby('origem_venda')['Valor Imposto'].agg('sum')
    df2=pd.merge(df2,df3,how = 'inner', on = 'origem_venda')
    df2['% Venda']=df2['% Venda'] = ((df2['Total R$'] / df2['Total R$'].sum()) * 100).round(0)
    return df2.rename(columns={'origem_venda':'Canal de Venda'})

def resumo_vendas(dt_inicial,dt_fim):
    df=vd.vendas(f"https://bling.com.br/Api/v3/pedidos/vendas?dataInicial={dt_inicial}&dataFinal={dt_fim}&pagina=")
    df2=pd.pivot_table(df[['Descr_situacao', 'origem_venda','total']],index=['origem_venda','Descr_situacao'], aggfunc="sum").rename(columns={'origem_venda':'Canal de Venda'})
    return df2

def resumo_nf(dt_inicial, dt_fim):
    df=nf.nota_fiscal(f"https://bling.com.br/Api/v3/nfe?dataEmissaoFinal={dt_fim}&dataEmissaoInicial={dt_inicial}&pagina=")
    return df