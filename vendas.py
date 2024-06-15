import pandas as pd
import canal_venda as cv
import impostos as imp
import produtos as prod
import extrair_informacoes as ext

dir=ext.ler_toml()['pastas']['dir']

def vendas(url,dt_inicial, dt_fim, status):
  df=pd.DataFrame()
  df_prod=pd.DataFrame(), pd.DataFrame()
  df_vendas=pd.read_parquet(f'{dir}pedidos_venda.parquet')
  df_vendas=df_vendas.drop(columns={'level_0', 'index'}).reset_index()
  df_vendas=df_vendas.query(f'data>="{dt_inicial}" and data<="{dt_fim}" and Descr_situacao=="{status}"')
  if len(df_vendas)>0:
    df_vendas = cv.canal_venda(df_vendas)
    #df_vendas = df_vendas.query(f'Descr_situacao=="{status}"')
    df=imp.incl_imposto(df_vendas)
    df_prod=prod.produtos_vendidos(df_vendas['id'].unique())
  #df_frete = prod.extrair_produtos_nf(df)[1]
  return df,df_prod[0],df_prod[1]

