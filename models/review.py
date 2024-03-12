#!/usr/bin/python3
"""the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Creates a new review which inherits from BaseModel
    The review Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The review test.
    """

    place_id = ""
    user_id = ""
    text = ""
