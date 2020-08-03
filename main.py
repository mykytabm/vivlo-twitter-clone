from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def dashboard():
    
    # displays  the stock  screener dashboard / homepage
    return {"Dashboard": "Home Page"}

@app.post("/stock") 
def create_stock():

    # created a stock and stores  it in database
    return{
        "code":"success",
        "message":"stock created"
    }