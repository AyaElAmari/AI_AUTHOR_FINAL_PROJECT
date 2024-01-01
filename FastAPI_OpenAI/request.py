import requests
import json

url = 'http://0.0.0.0:8000/check'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
data = {
    "text": "Ayah"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())

