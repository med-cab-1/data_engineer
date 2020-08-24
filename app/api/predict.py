import logging
import random

from fastapi import APIRouter
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
async def predict(item: Item):
    """
    Drop down menus for the Following:

    1- Desired Affects: Decreasing Depression
    2- Body affects:
    3- Mood alteration:
    4- Appetite stimulation
    5-
    """

    X_new = item.to_df()
    log.info(X_new)
    y_pred = random.choice([True, False])
    y_pred_proba = random.random() / 2 + 0.5
    return {
        'prediction': y_pred,
        'probability': y_pred_proba
    }
