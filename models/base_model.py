#!/usr/bin/python3
'''
BaseModel class module which will be the base class
of all instances created
which are AirBnB related as states rooms etc..
'''


import models as mdl
import uuid
from datetime import datetime


class BaseModel:
    '''
    BaseModel Class which will
    be the base class for everything
    else in this project
    '''

    def __init__(self, *args, **kwargs):
        '''
        Init function for BaseModel instances
        and will initializae depending
        of the arguments given between args and kwargs
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
            mdl.storage.new(self)

    def __str__(self):
        '''
        String represantation of the instance
        created [ClassName] (id) {dictionary}
        '''

        string = "[{}]".format(self.__class__.__name__)
        string += " ({}) {}".format(self.id, self.__dict__)
        return string

    def save(self):
        '''
        Function to update the update_at
        attribute of the instance when
        updated
        '''

        self.updated_at = datetime.now()
        mdl.storage.save()
        return self.updated_at

    def to_dict(self):
        '''
        Dictionary represantation of the instace
        containing all its values and the datetimes
        will be converted in readeble format
        '''

        format = "%Y-%m-%dT%H:%M:%S.%f"
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = data['created_at'].strftime(format)
        data['updated_at'] = data['updated_at'].strftime(format)
        return data
