import os
import datetime
import streamlit as st

import tomllib
import requests

today=datetime.date.today()
dia=datetime.timedelta(1)
with open(os.path.basename('C:\PlenoLed\secrets.toml'), "rb") as f:
        valores = tomllib.load(f)
st.write(valore)



