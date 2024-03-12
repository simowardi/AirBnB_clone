#!/usr/bin/python3
"""the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Creates a new amenity which inherity from BaseModel
    The amenity Attributes:
    name (str): The amenity name.
    """

    name = ""
