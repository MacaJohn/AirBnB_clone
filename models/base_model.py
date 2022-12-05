#!/usr/bin/python3
"""A module that implements the BaseModel class"""
from uuid import uuid4
from datetime import datetime

<<<<<<< HEAD
=======

class BaseModel:
    """
        The Base model class
        Methods:
            __init__ - the constructor method
            __str__ - the informal representation of the class
            save: function updates the updated_at attribute
            to_dict: returns the dictionary representation of the string
    """
>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb

class BaseModel:
    """A class that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
<<<<<<< HEAD
=======
        """ The constructor method of the BaseModel class """

        from models import storage

>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
        if not kwargs:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            del kwargs["__class__"]
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__.update(kwargs)

    def __str__(self):
        """
        Returns the string representation of BaseModel object.
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
<<<<<<< HEAD
        """Updates 'self.updated_at' with the current datetime"""
=======
        """ edits the updated_at attribute of the BaseModel class"""

>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance:
               - only instance attributes set will be returned
               - a key __class__ is added with the class name of the object
               - created_at and updated_at must be converted to string object
                            in ISO object
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                value = self.__dict__[key].isoformat()
                my_dict[key] = value
        return my_dict
