import io
import requests
import base64
import os
import tomllib

def ler_toml():
    with open(r"C:\PlenoLed\secrets.toml", "rb") as f:
        valores = tomllib.load(f)
    return valores

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization':f"{ler_toml()['credenciais']['token']}",
  'Cookie': f"{ler_toml()['credenciais']['Cookie']}"
}
def extrai(url):
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code!=200:
        if response.json()['error']['description']=='The access token provided has expired':
            response_token=refreshToken()
    return response

def refreshToken():
    CLIENT_ID = "c96ea6eba958d42819fe0faf06e50a0db499ca54"
    CLIENT_SECRET = "ee90ba8bb6bcd8622300eebcc0b45044879eaa84718abf2b34c2fbbb12ff"
    REDIRECT_URI = "https://www.google.com/"
    STATE=42
    refresh_token=ler_toml()['credenciais']['refresh']

    base64_encoded_clientid_clientsecret = base64.b64encode(str.encode(f'{CLIENT_ID}:{CLIENT_SECRET}'))
    base64_encoded_clientid_clientsecret = base64_encoded_clientid_clientsecret.decode('ascii')
    url = f"https://bling.com.br/Api/v3/oauth/token"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': f'Basic {base64_encoded_clientid_clientsecret}'
    }
    data = {'grant_type': 'refresh_token',
            'redirect_uri': REDIRECT_URI,
            'refresh_token': refresh_token
            }
    r = requests.post(url, headers=headers, data=data)
    print(r.json())
    response = r.json()


def salvar_toml(response):
    user = os.getlogin()
    with io.open(fr'c:\PlenoLed\secrets2.toml', "w", encoding="utf-8") as file:
        file.write(str())



