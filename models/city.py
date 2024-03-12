#!/usr/bin/python3
"""the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Creates a new city which inherits from BaseModel
    The city Attributes:
        state_id (str): Thed of the state.
        name (str): The city name.
    """

    state_id = ""
    name = ""
