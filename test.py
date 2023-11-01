import requests
from uuid import uuid4

print(uuid4())
url = "http://127.0.0.1:8000/api/note/create"
params = {
    "user_id": "7765fcd23fad0aeab10f145d",
    "target_id": '0',
    "key": 'regi'
}
headers = {
    "accept": "application/json"
}

response = requests.post(url, params=params, headers=headers)

if response.status_code == 200:
    print("Успешный запрос!")
    data = response.json()
    print(data)
