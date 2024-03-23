#!/usr/bin/py

"""
module to house Review class that
inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review model that defines the blueprint
    for all review instance
    """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
