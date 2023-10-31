#!/usr/bin/python3

import models
import uuid
from datetime import datetime

class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datatime.now()
        self.update_at = self.created_at
    
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