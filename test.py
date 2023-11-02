import asyncio
import time

import requests

async def make_request(url, params, headers):
    response = requests.post(url, params=params, headers=headers)
    time.sleep(2)
    if response.status_code == 200:
        data = response.json()
        print(f"Успешный запрос: {data}")
    else:
        print(f"Ошибка запроса: {response.status_code}")

async def main():
    urls = ["http://127.0.0.1:8000/api/note/create"] * 30  # Создайте список URL-адресов
    params = {
        "user_id": "7765fcfaa0f14",
        "target_id": '0',
        "key": 'new_login'
    }
    headers = {
        "accept": "application/json"
    }

    tasks = []
    for url in urls:
        task = asyncio.create_task(make_request(url, params, headers))
        tasks.append(task)

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
