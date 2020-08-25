import logging
import random

from fastapi import APIRouter
from fastapi.responses import JSONResponse
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()

"""
Code below is in progress, currently coommented out to prevent errors
when deploying to Heroku
"""


# class DesiredAffects(BaseModel):
#     """Use this data model to parse the request body JSON."""
#
#     Desired_Affect1: str = Field(..., example='Mood Alteration')
#     Desired_Affect2: str = Field(..., example='Body Relaxation')
#     Desired_affect3: str = Field(..., example='Creativity')
#
#     def to_df(self):
#         """Convert pydantic object to pandas dataframe with 1 row."""
#         return pd.DataFrame([dict(self)])
#
#     @validator('x1')
#     def x1_must_be_positive(cls, value):
#         """Validate that x1 is a positive number."""
#         assert value > 0, f'x1 == {value}, must be > 0'
#         return value


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    x1: float = Field(..., example=3.14)
    x2: int = Field(..., example=-42)
    x3: str = Field(..., example='banjo')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    @validator('x1')
    def x1_must_be_positive(cls, value):
        """Validate that x1 is a positive number."""
        assert value > 0, f'x1 == {value}, must be > 0'
        return value


@router.post('/predict')
async def predict(item: Item):
    """
    Drop down menus for the Following:

    Rated Each feature importance:
    """

    x_df = item.to_df()
    y_pred = 'OG Kush'  # ML model would output the most desirable strain here
    y_pred_proba = 'OG Kush matches your desired affect to 98% accuracy'  # here we would describe how closely it fits
    return {
        'prediction': y_pred,
        'probability': y_pred_proba
        # 'Hello, World!''
    }


@router.get('/predict')
async def test_prediction():
    demo_response = {
        'strain': {
            'name': 'Grandaddy Purple',
            'type': 'Indica',
            'description': 'Makes you sleep',
            'Terpenes': ['Herbal', 'Peppery', 'Pine'],
            'Effect': 'Calming'
        }
    }

    return JSONResponse(content=demo_response)
