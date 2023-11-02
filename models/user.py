#!/usr/bin/python3
"""
This defines a BaseModel class for managing the data.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '''
        Init function
        '''

        super().__init__(*args, **kwargs)
