#!/usr/bin/env python3
""" This module contains the BaseModel class"""
from datetime import datetime
from uuid import uuid4

class BaseModel:
    """
        The Base model class
        Methods:
            __init__ - the constructor method
            __str__ - the informal representation of the class
            save: function updates the updated_at attribute
            to_dict: returns the dictionary representation of the string
    """

    def __init__(self, *args, **kwargs):
        """ The constructor method of the BaseModel class """
        
        from models import storage

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """Returns the informal string representation of this class """
        this_class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(this_class_name, self.id, self.__dict__)

    def save(self):
        """ edits the updated_at attribute of the BaseModel class"""
        
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns the dictionary representation of this class"""
        my_dict = self.__dict__.copy()
        my_dict.update({'__class__': self.__class__.__name__})
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict
