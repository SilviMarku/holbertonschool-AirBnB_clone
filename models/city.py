#!/usr/bin/python3
"""
This defines a class City that inherits from BaseModel.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    This represents a city with state_id and name attributes.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Inicialize a City instance that inherits initialization from BaseModel.
        """
        super().__init__(*args, **kwargs)
