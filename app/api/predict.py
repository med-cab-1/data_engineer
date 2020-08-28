#! usr/bin/python3


# IMPORTS
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



"""
Predict file that contains code and routes for when the server recieves a
predict request from the user.
"""

# Logging configuration
log = logging.getLogger(__name__)


# FastAPI route setup
router = APIRouter()


class Input(BaseModel):
    """
    Use this data model to parse the JSON request body.

    JSON PARAMETERS:
        input_phrase: str
    """
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
    pred = train(user_input.input_phrase)

    # Create query string
    query_strain = curs.execute(f"SELECT * FROM Cannabis WHERE Strain_ID == {pred} ORDER BY Rating")
    # Send query  to database
    strain = curs.fetchall()
    # Response formatting
    keys = ['ID', 'Strain_id', 'Name', 'Type', 'Rating', 'Effects', 'Description', 'Flavors', 'Neighbors']
    suggestion = {k: v for k, v in zip(keys, strain[0])}
    for key in ['Effects', 'Flavors', 'Neighbors']:
        suggestion[key] = suggestion[key].split(',')
    # Return our response with JSONResponse
    return JSONResponse(content=suggestion)


@router.post('/test')
async def test(user_input: Input):
    """
    Test route per front end request to be able to receive dummy data.
    The dummy data is a valid query from the db, just with a hardcoded
    prediction.
    """

    conn = sqlite3.connect('Data/cannabis.sqlite3')
    curs = conn.cursor()

    pred = 420
    # Create query string
    query_strain = curs.execute(f"SELECT * FROM Cannabis WHERE Strain_ID == {pred} ORDER BY Rating")
    # Send query  to database
    strain = curs.fetchall()
    # Response formatting
    keys = ['ID', 'Strain_id', 'Name', 'Type', 'Rating', 'Effects', 'Description', 'Flavors', 'Neighbors']
    suggestion = {k: v for k, v in zip(keys, strain[0])}
    for key in ['Effects', 'Flavors', 'Neighbors']:
        suggestion[key] = suggestion[key].split(',')
    # Return our response with JSONResponse
    return JSONResponse(content=suggestion)

@router.get('/init_db')
async def init_db():
    """
    Function for creating a database for local operation
    Calls the create_db() function from our init_db file.
    """
    create_db()


if __name__ == '__main__':
    """
    For localized testing.
    """
    create_db()
