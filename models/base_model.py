#!/usr/bin/python3
"""Base model module"""


import uuid
from datetime import datetime


class BaseModel:
    """Defines the BaseModel class"""

    def __init__(self):
        """Constructor method for the BaseModel class.
        Initializes the instance's unique id and saves the datetime of
        creation and update"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Overwrites the __str__ method"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of
        the instance"""
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()

        return self.__dict__
