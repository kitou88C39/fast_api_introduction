from fastapi import FastAPI

app = FastAPI()

@app.get("/") # HTTPリクエストメソッド GETに対する関数
def read_root():
    return {"message": "APIです"}