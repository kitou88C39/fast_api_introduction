from fastapi import FastAPI

app = FastAPI()

def read_root():
    return {"message": "APIです"}