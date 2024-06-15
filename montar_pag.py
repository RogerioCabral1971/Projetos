import pandas as pd
import streamlit as st
import relatorio_plenoled as rel

def formatar_num(valor):
    valor_frmt="{:,.2f}".format(valor).replace(',','_').replace('.',',').replace('_','.')
    return valor_frmt


def cartao_resumo(df):
    df=pd.DataFrame(df).reset_index()
    colunas = ['col1', 'col2', 'col3', 'col4']
    colunas = st.columns(4)
    colunas[0].metric(f"TOTAL VENDA BRUTA - {df['Quantidade Venda'].sum()} Vendas", f"R$ {formatar_num(df['Total R$'].sum().round(0))}")
    colunas[0].text(f"TOTAL IMPOSTO R$ {formatar_num(df['Impostos'].sum())}")
    venda_liq_total=f"Venda Líquida R$ {formatar_num(df['Total R$'].sum()-df['Impostos'].sum())}"
    colunas[0].markdown(f'''##### _:gray[{venda_liq_total}]_''')
    for idx in df['Canal de Venda'].index:
        colunas[idx+1].metric(f"{str(df['Canal de Venda'][idx]).upper()} - {df['Quantidade Venda'][idx]} Vendas", f"R$ {formatar_num(df['Total R$'][idx])}")
        colunas[idx+1].text(f"Imposto R$ {formatar_num(df['Impostos'][idx])}")
        venda_liq_canal=f"Venda Líquida R$ {formatar_num(df['Total R$'][idx] - df['Impostos'][idx])}"
        colunas[idx+1].markdown(f'''###### _:gray[{venda_liq_canal}]_ ''')

def tabela_resumo(df,inicial,fim):
    df=st.data_editor(df,key='tabresumo')
    st.data_editor(rel.resumo_nf(inicial,fim))

def tabela_produto(df,df_frete):
    df=pd.DataFrame(df).reset_index()
    #df2=df.groupby('descricao')['quantidade'].agg('sum')
    #st.data_editor(df2)
    st.data_editor(df[['codigo', 'descricao','quantidade','R$ Total']], hide_index=True, width=1200, height=1200,
                   column_config={"R$ Total": {"alignment": "center"}, "quantidade": {"alignment": "center"}})




