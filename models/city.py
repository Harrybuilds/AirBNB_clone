#!/usr/bin/python3

"""
module to house City class that
inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City model that defines the blueprint
    for all city instance
    """
    state_id: str = ""
    name: str = ""
