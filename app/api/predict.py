import logging
import random
import pandas
import sqlite3
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import pandas as pd
from pydantic import BaseModel, Field, validator
from .init_db import create_db, say_hi
from .model import train

log = logging.getLogger(__name__)
router = APIRouter()

"""
Code below is in progress, currently commented out to prevent errors
when deploying to Heroku
"""


class Input(BaseModel):
    """Use this data model to parse the request body JSON."""
    input_phrase: str


@router.post('/predict')
async def test_prediction(user_input: Input):
    # conn = sqlite3.connect('../../Data/cannabis.sqlite3')
    conn = sqlite3.connect('Data/cannabis.sqlite3')
    curs = conn.cursor()
    # pred = 687  # Stable prediction before the model goes into place
    # pred = model.predict(user_input.input_phrase)
    print(user_input.input_phrase)
    pred = train(user_input.input_phrase)

    # strains = []
    # for p in pred:
    #     query_strain = curs.execute(f"SELECT * FROM Cannabis WHERE Strain_ID == {p} ORDER BY Rating")
    #     strain = curs.fetchall()
    #     keys = ['ID', 'Strain_id', 'Name', 'Type', 'Rating', 'Effects', 'Description', 'Flavors', 'Neighbors']
    #     suggestion = {k: v for k, v in zip(keys, strain[0])}
    #     for key in ['Effects', 'Flavors', 'Neighbors']:
    #         suggestion[key] = suggestion[key].split(',')
    #     strains.append(suggestion)

    query_strain = curs.execute(f"SELECT * FROM Cannabis WHERE Strain_ID == {pred} ORDER BY Rating")
    strain = curs.fetchall()
    keys = ['ID', 'Strain_id', 'Name', 'Type', 'Rating', 'Effects', 'Description', 'Flavors', 'Neighbors']
    suggestion = {k: v for k, v in zip(keys, strain[0])}
    for key in ['Effects', 'Flavors', 'Neighbors']:
        suggestion[key] = suggestion[key].split(',')



    return JSONResponse(content=suggestion)


@router.get('/init_db')
async def init_db():
    create_db()

@router.get('/test')
async def hello():
    train()


if __name__ == '__main__':
    create_db()
