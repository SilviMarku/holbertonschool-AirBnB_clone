#!/usr/bin/python3
"""
Defines a State class that inherits from BaseModel.
"""


from models.base_model import BaseModel


class State(BaseModel):
    '''
    State class which inherits from
    BaseModel
    '''
    name = ""

    def __init__(self, *args, **kwargs):
        '''
        Init function
        '''
        super().__init__(*args, **kwargs)
