import pandas as pd
import extrair_informacoes as ext

dir=ext.ler_toml()['pastas']['dir']


def canal_venda(df):
    canal_venda_local=pd.read_parquet(f'{dir}canais_venda.parquet')
    #canalvenda = "https://bling.com.br/Api/v3/canais-venda"
    #response_canais = requests.request("GET", canalvenda, headers=headers, data=payload)
    #df_canais = pd.DataFrame(response_canais.json()['data'])
    df_canais=canal_venda_local
    id_canal=[]
    origem_venda=[]

    for id in df['loja'].index:
      id_canal.append(list(df['loja'])[0]['id'])
      try:
        origem_venda.append(list(df_canais[df_canais['id']==df['loja'][id]['id']]['descricao'])[0])
      except:
          origem_venda.append('Comercial')
    df['canal']=id_canal
    df['origem_venda']=origem_venda
    return df