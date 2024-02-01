from fastapi import FastAPI

app = FastAPI()

@app.get("/") # HTTPリクエストメソッド GETに対する関数
def read_root():
    return {"message": "APIです"}

# パラメータを作成する
@app.get("/items/{item_id}")
def read_item(item_id):
    return{"item_id":item_id, "item_name":"Tシャツ"}
    
# クエリパラメータを作成する
@app.get("/items")
def read_item():