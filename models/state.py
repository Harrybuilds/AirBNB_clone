#!/usr/bin/py

"""
module to house State class that
inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State model that defines the blueprint
    for all state instance
    """
    name: str = ""
