import request

res = requests.get("http://127.0.0.1:8000/items/111")

print(res.status_code)
print(res.text)

# クエリパラメータを作成する
res = requests.get("http://127.0.0.1:8000/items/?skip=1&limit=2")

print(res.status_code)
print(res.text)

# POSTを使ってリクエストボディを使う方法
import requests

res = requests.post(
    "http://127.0.0.1:8000/items/",
    json={"name": "Tシャツ", "price":2000, "description":"白Tシャツ"},
)

print(res.status_code)
print(res.text)

# ヘッダーとはリクエストやレスポンスにおいて付加情報を伝えるもの
import requests

res = requests.get(
    "http://127.0.0.1:8000/sample/",
    headers={"authorization": "Bearer: A1B2C3D4"},
)

print(res.status_code)
print(res.text)
print(res.headers)

# 非同期処理
import requests
import asyncio
import time

if __name__=="__main__":
    asyncio.run(main())

