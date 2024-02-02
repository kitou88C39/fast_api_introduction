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
app = FastAPI()
items = ["Tシャツ","スカート","ブーツ"]

@app.get("/items")
def read_items(skip: int = 0, limit: Annotated[int, Query(ge=1, le=10)]=10):
    return {"item": items[skip : skip + limit]}

# POSTを使ってリクエストボディを使う方法
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: Union[str, Nome] = Nome

@app.post("/items/")
def create_item(item: Item):
    print(f"データを登録します:{item.name},{item.price},{item.description}")
    return item

# ヘッダーとはリクエストやレスポンスにおいて付加情報を伝えるもの
from fastapi import FastAPI, Header
from typing import Union

app = FastAPI()

@app.get("/sample/")
def read_sample(
    response: Response,
    authorization: Union[str, Nome]= Header(defalut=Nome)
    ):
    print(authorization)
    response.headers["custom-header"]="12345"
    return {"message":"ヘッダー情報を取得する"}