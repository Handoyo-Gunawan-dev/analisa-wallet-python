from fastapi import FastAPI
from analisa import analisa_wallet
import os

app=FastAPI()

@app.get("/")
def root():
    return{"message":"API jalan"}

@app.get("/analisa")
def analisa(file:str):
    if not os.path.exists(file):
        return {"error": "file tidak ditemukan"}
    
    
    hasil=analisa_wallet(file)

    return hasil    