#!usr/bin/python3
'''
FileStorage module for FileStorage class
and its functionalities this class will be used
to deserialiaze and serialize Models objects
'''

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    '''
    FileStorage class which will
    serve as a storage for
    all instances created
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
        Instance method to return
        objects dictionary
        '''

        return FileStorage.__objects

    def new(self, obj):
        '''
        Instance method to add obj created at
        objects dictionary
        '''

        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
        return True

    def save(self):
        '''
        Instance method to serialize objects
        to the JSON file: __file_path
        '''

        obj_dictionary = {key: value.to_dict() for key,
                          value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dictionary, file)
        return True

    def reload(self):
        '''
        Instance method to
        deserialiaze file
        '''

        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name, obj_id = key.split('.')
                    obj = eval(cls_name)(**value)
                    self.new(obj)
                return True
        except Exception as e:
            pass
            return False
