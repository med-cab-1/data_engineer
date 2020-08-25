import logging
import random

from fastapi import APIRouter
from fastapi.responses import JSONResponse
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class DesiredAffects(BaseModel):
    """Use this data model to parse the request body JSON."""

    Desired_Affect1: str = Field(..., example='Mood Alteration')
    Desired_Affect2: str = Field(..., example='Body Relaxation')
    Desired_affect3: str = Field(..., example='Creativity')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    @validator('x1')
    def x1_must_be_positive(cls, value):
        """Validate that x1 is a positive number."""
        assert value > 0, f'x1 == {value}, must be > 0'
        return value


@router.post('/predict')
async def predict(item: DesiredAffects):
    """
    Drop down menus for the Following:

<<<<<<< HEAD
    ### Request Body
    - `x1`: positive float
    - `x2`: integer
    - `x3`: string

    ### Response
    - `prediction`: boolean, at random
    - `predict_proba`: float between 0.5 and 1.0,
    representing the predicted class's probability

    Replace the placeholder docstring and fake predictions with your own model.
=======
    1- Bodily Affects: Tingly, Energetic, Relaxed
    2- Mind affects: Happy, Euphoric,
    3- Mood alteration: Uplifted, Giggly, Focused
    4- Taste: Earthy, Woody, Pine, Grape, Sweet, Pungent
    5- THC:CBD Ratio: 1:1, 1:10, 1:20, 3:1, 5:1, 10:1
>>>>>>> 8c74bbf107eceae9f27b226ef55325b7ea0c2408
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
