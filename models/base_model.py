#!/usr/bin/python3
'''
BaseModel class module which will be the base class of all instances created
which are AirBnB related as states rooms etc..
'''


import models
import uuid
from datetime import datetime


class BaseModel:
    '''
    BaseModel Class
    '''

    def __init__(self, *args, **kwargs):
        '''
        Init function for BaseModel instances
        '''

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                    if key == 'created_at' or key == "updated_at":
                        setattr(self, key, datetime.fromisoformat(value))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''
        String represantation of the instance
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        Function to update the update_at
        attribute of the instance when
        updated
        '''

        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        Dictionary represantation of the instance
        '''

        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = data['created_at']\
            .strftime("%Y-%m-%dT%H:%M:%S.%f")
        data['updated_at'] = data['updated_at']\
            .strftime("%Y-%m-%dT%H:%M:%S.%f")
        return data
