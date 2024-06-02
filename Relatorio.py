import pandas as pd
import vendas as vd

def resumo_canal(dt_inicial,dt_fim, status_pedido):
    df=vd.vendas(f"https://bling.com.br/Api/v3/pedidos/vendas?dataInicial={dt_inicial}&dataFinal={dt_fim}&pagina=")
    df2=df.query(f'Descr_situacao=="{status_pedido}"').groupby(
        'origem_venda').total.agg(['count','sum','mean' ]
                                  ).rename(columns={
        'count':'Quantidade Venda','sum':'Total R$', 'mean':'Media R$'})
    df2.reset_index(inplace=True)
    df2['% Venda']=df2['% Venda'] = ((df2['Total R$'] / df2['Total R$'].sum()) * 100).round(0)
    #print(df2.rename(columns={'origem_venda':'Canal de Venda'}))
    return df2.rename(columns={'origem_venda':'Canal de Venda'})

def resumo_vendas(dt_inicial,dt_fim):
    df=vd.vendas(f"https://bling.com.br/Api/v3/pedidos/vendas?dataInicial={dt_inicial}&dataFinal={dt_fim}&pagina=")
    df2=pd.pivot_table(df[['Descr_situacao', 'origem_venda','total']],index=['origem_venda','Descr_situacao'], aggfunc="sum").rename(columns={'origem_venda':'Canal de Venda'})
    return df2
    #print(df2)
