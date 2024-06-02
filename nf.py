import requests
import pandas as pd
from vendas import token
payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 7fe30c52d2b20d4e1488d0188c90e331f45a9f49',
  'Cookie': 'PHPSESSID=15de1ths4uag634bfr9fcqhivm'
}
def nota_fical():
    nf = "https://bling.com.br/Api/v3/nfe"
    response_nf = requests.request("GET", nf, headers=headers, data=payload)
    df_nf=pd.DataFrame(response_nf.json()['data'])
    return df_nf