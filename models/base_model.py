#!/usr/bin/python3

import models
import uuid
from datetime import datetime

class BaseModel:
    #!/usr/bin/python3

import models
import uuid
from datatime import datatime

class BaseModel:
    
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
    
    def __str__(self):
        return f"[{self.__class__.name}] ({self.id}) {elf.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):

        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = data['created_at'].isoformat()
        data['apdated_at'] = data['apdated_at'].isoformat()

    
    
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {elf.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):

        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = data['created_at'].isoformat()
        data['updated_at'] = data['updated_at'].isoformat()
        return data 