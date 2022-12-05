<<<<<<< HEAD
#!/usr/bin/python3
"""This module defines a class User"""
=======
#!/usr/bin/env python3
""" holds class User """
>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
=======
    """Representation of a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """constructor of the User class"""
        super().__init__(*args, **kwargs)
>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
