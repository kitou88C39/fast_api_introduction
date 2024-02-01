import request

res = requests.get("http://127.0.0.1:8000/items/111")

print(res.status_code)
print(res.text)

# クエリパラメータを作成する

res = requests.get("http://127.0.0.1:8000/items/?skip=1&limit=2")

print(res.status_code)
print(res.text)