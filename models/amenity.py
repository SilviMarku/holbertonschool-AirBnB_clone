#!/usr/bin/python3
"""
This defines an Amenity class that inherits from BaseModel.
"""


from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    A class variable for 'name' with an initial value of an empty string
    """
    name + ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a Amenity instance, that inherits initialization from BaseModel.
        """
        super().__init__(*args, **kwargs)
    