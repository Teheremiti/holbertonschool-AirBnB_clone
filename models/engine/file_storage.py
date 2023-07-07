#!/usr/bin/python3
"""FileStorage class module"""


import json
import os.path


class FileStorage:
    """Defines the FileStorage class

    Class attributes:
        file_path (str): Private. Path to the JSON file
        objects (dict): Private. Stores all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id

        Args:
            obj (obj): A FileStorage object
        """

        attr = type(obj).__name__ + "." + obj.id
        self.__objects[attr] = obj

    def save(self):
        """Serializes __objects to the JSON file"""

        json_dict = {}
        for attr, value in self.__objects.items():
            json_dict[attr] = value.to_dict()

        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(json_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        from models import base_model
        from models import user
        from models import state
        from models import city
        from models import amenity
        from models import place
        from models import review

        modules = {
            "BaseModel": base_model,
            "User": user,
            "State": state,
            "City": city,
            "Amenity": amenity,
            "Place": place,
            "Review": review
        }

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for attr, value in json.load(f).items():
                    if cls in modules:
                        cls = getattr(modules[cls], value["__class__"])

                    obj = cls(**value)
                    self.__objects[attr] = obj
