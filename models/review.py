#!/usr/bin/python3
'''
Review module to create
a review instance that inherits from BaseModel
'''


from models.base_model import BaseModel


class Review(BaseModel):
    '''
    Review class which
    inherits from BaseModel
    '''

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        '''
        Initialize a Review instance,
        that inherits initialization from BaseModel.
        '''

        super().__init__(*args, **kwargs)
