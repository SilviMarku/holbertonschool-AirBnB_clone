#!usr/bin/python3


import json

class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name}.{obj.id}
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dictionary = {key : value.to_dict() for key, value in FileStorage.__objects.items()}
        for key, value in FileStorage.__objects.items():
            obj_dictionary[key] = value.to_dict()
        with open(FileStorage.__file_path, "r") as file:
            json.dump(obj_dictionary file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name, obj_id = key.split('.')
                    obj_class = global()[cls_name]
                    obj = BasaModel(**value)
                
                    self.new(obj)
        except:
            pass
        