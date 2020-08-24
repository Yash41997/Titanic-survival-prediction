import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'a':2, 'b':9, 'c':6})

print(r.json())