import extrair_informacoes as extr
import pandas as pd
import streamlit as st
dir=extr.ler_toml()['pastas']['dir']

def produtos_vendidos(id):
    df_itens = pd.DataFrame()
    frete = []
    df_nf = pd.read_parquet(f'{dir}notas_fiscais.parquet')
    df_nf=df_nf.drop(columns={'index', 'level_0'})
    df_nf=df_nf.query(f'id in {list(id)}')
    df_nf=df_nf.reset_index()
    for idx in df_nf.index:
        df = pd.DataFrame(list(df_nf['itens'][idx]))
        df['canal_origem']=str(df_nf['loja'][idx]['id'])
        df_itens = pd.concat([df_itens, df])
        frete.append(df_nf['transporte'][idx]['frete'])
    df_itens['R$ Total']=df_itens['quantidade']*df_itens['valor']
    colunas=['canal_origem','codigo', 'descricao', 'quantidade', 'valor', 'desconto', 'R$ Total']
    return df_itens[colunas].sort_values(by='quantidade',ascending=False), sum(frete)


def extrair_produtos_nf(df):
    url = "https://bling.com.br/Api/v3/pedidos/vendas/"
    my_bar = st.progress(0, text="progress_text")
    df2=pd.DataFrame()
    df2_transp=pd.DataFrame()
    cont=0
    for id in df['id']:
        cont=cont+1
        if cont==100:
            cont=1
        my_bar.progress(cont, text=f'Mercadoria lida...: {cont}')
        response=extr.extrai(url+str(id))
        lista_itens=response.json()['data']['itens']
        lista_transp=response.json()['data']['transporte']
        df=pd.DataFrame(lista_itens)
        df_transp=pd.DataFrame([lista_transp])
        df2=pd.concat([df,df2], ignore_index=True)
        df2_transp=pd.concat([df_transp,df2_transp], ignore_index=True)
        colunas=['quantidade','desconto','valor','descricao','produto']
    my_bar.empty()
    return df2[colunas].sort_values(by='quantidade',ascending=False),df2_transp['frete'].sum()
