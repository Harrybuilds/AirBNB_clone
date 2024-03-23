#!/usr/bin/python3

"""
module to houses the User class that
inherits from BaseModel class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that defines the blue printfor a user
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
