#!/usr/bin/env python3
""" This module contains the file storage class """
import json
from models.base_model import BaseModel


class FileStorage:
    """
        FileStorage class
        private instance variables
        __file_path: will hold the path to the file
        __object: will hold deserialized objects
    """
    __file_path = "storage.json"
    __objects = {}

    def __init__(self):
        """ The constructor method of the FileStorage class """
        pass

    def all(self):
        """ This method returns the content of __objects variable """
        return self.__objects

    def new(self, obj):
        """
            updates the content of __object variable
            Argument:
                obj: the object to be updated to the variable
        """
        if obj is not None:
            obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[obj_key] = obj

    def save(self):
        """ saves a serialized python dictionary object to a json file """
        with open(self.__file_path, "w", encoding="utf-8") as json_file:
            obj_dict = {}
            for key, val in self.__objects.items():
                obj_dict[key] = val.to_dict()
            json.dump(obj_dict, json_file)

    def reload(self):
        """
            loads a deserialized string from a json file (only if it exists)
            to the object variable
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as json_file:
                for obj in json.load(json_file).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            pass
