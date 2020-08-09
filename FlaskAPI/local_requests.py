
import requests
from X_input import data_inputs

URL = 'http://127.0.0.1:5000/predict'

head = {"Content-Type": "application/json"}
data = {"input" : data_inputs}

r = requests.get(URL,headers = head, json = data )

r.json()