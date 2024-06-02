import requests
import pandas as pd

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': token,
  'Cookie': Cookie
}
def nota_fical():
    nf = "https://bling.com.br/Api/v3/nfe"
    response_nf = requests.request("GET", nf, headers=headers, data=payload)
    df_nf=pd.DataFrame(response_nf.json()['data'])
    return df_nf
