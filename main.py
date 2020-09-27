import models

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from database import SessionLocal, engine   
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

@app.get("/")
def dashboard(request:Request):

    # displays  the stock  screener dashboard / homepage
    return templates.TemplateResponse("dashboard.html",{
        "request":request
    })


@app.post("/stock")
def create_stock():

    # created a stock and stores  it in database
    return{
        "code": "success",
        "message": "stock created"
    }
