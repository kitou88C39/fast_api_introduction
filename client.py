import request

res = requests.get("http://127.0.0.1:8000/items/111")

print(res.status_code)
print(res.text)