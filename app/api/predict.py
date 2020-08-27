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
Predict file that contains code and routes for when the server recieves a
predict request from the user.


"""


class Input(BaseModel):
    """Use this data model to parse the request body JSON."""
    input_phrase: str


@router.post('/predict')
async def predict(user_input: Input):
    """
    Function for taking in the user input string containing from the http request
    body and sending the string containing the key words to the model for
    predicting a suggested strain.

    
    """

    # Setup and configure our connection to our database
    conn = sqlite3.connect('Data/cannabis.sqlite3')
    curs = conn.cursor()

    # Uncomment code below to use our model to obtain live predictions
    # pred = train(user_input.input_phrase)
    pred = 420
    """
    Commented code below is for use if we want to return more than one
    prediction.
    """
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


if __name__ == '__main__':
    create_db()
