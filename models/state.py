#!/usr/bin/python3
"""The State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Creates a new state that inherits from BaseModel
    The state Attributes:
        name (str): The state name.
    """

    name = ""
