#!/usr/bin/python3
"""The User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """User attribute:
        email (str): The user email.
        password (str): The user password.
        first_name (str): The user first name.
        last_name (str): The user last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
