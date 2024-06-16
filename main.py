import os
import datetime
import streamlit as st

import tomllib
import requests

today=datetime.date.today()
dia=datetime.timedelta(1)

st.write(os.path.basename('C:\PlenoLed\secrets.toml'))



