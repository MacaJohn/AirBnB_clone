#!/usr/bin/env python3
""" This module contains the BaseModel class"""
import datetime
import uuid

class BaseModel:
    """
        The Base model class
        Methods:
            __init__ - the constructor method
            __str__ - the informal representation of the class
            save: function updates the updated_at attribute
            to_dict: returns the dictionary representation of the string
    """

    def __init__(self):
        """ The constructor method of the BaseModel class """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns the informal string representation of this class """
        this_class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(this_class_name, self.id, self.__dict__)

    def save(self):
        """ edits the updated_at attribute of the BaseModel class"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns the dictionary representation of this class"""
        my_dict = self.__dict__.copy()
        my_dict.update({'__class__': self.__class__.__name__})
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict

