from typing import Optional
from fastapi import FastAPI
from fastapi.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import urllib.parse
# from app.queries import get_cards
from queries import get_cards

description = """
Las distintas APIs que componen el proyecto de Ecobici. 🚲
"""

app = FastAPI(
    title="Dashboard de Ecobici.",
    description=description,
    vesrion="0.0.1"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/cards/{trip_year}")
def read_cards(año:Optional[int]=2021, mes:Optional[int]=None, dia:Optional[int]=None):

    if año == 2018:
        q1=f'trip_year > {año}'
    else:
        q1=f'trip_year = {año}'
    
    if mes:
        q2 = f" AND trip_month = {mes}"
    else:
        q2="" 
    
    if dia:
        q3= f" AND trip_day = {dia}"
    else:
        q3=""

    query = f"{q1}{q2}{q3}"

    
    # print(query)

    cards = get_cards(cardsdate=f"mes = {mes} and dia = {dia}")
 
    return{
        "cardsData":cards
    }

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}