#!/usr/bin/py

"""
module to house Amenity class that
inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity model that defines the blueprint
    for all amenity instance
    """
    name: str = ""
