<<<<<<< HEAD
#!/usr/bin/python3
""" State Module for HBNB project """
=======
#!/usr/bin/env python3
""" The module of the state class """
>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
from models.base_model import BaseModel


class State(BaseModel):
<<<<<<< HEAD
    """ State class """
    name = ""
=======
    """Representation of state """
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor of the state class"""
        super().__init__(*args, **kwargs)
>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
