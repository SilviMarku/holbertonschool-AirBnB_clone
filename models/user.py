#!/usr/bin/python3
'''
This defines a BaseModel class for managing the data.
'''


from models.base_model import BaseModel


class User(BaseModel):
    '''
    User class that inherits from BaseModel
    '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '''
        Initialize a Amenity instance,
        that inherits initialization from BaseModel.
        '''

        super().__init__(*args, **kwargs)
