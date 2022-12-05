<<<<<<< HEAD
#!/usr/bin/python3
""" City Module for HBNB project """
=======
#!/usr/bin/env python3
""" City class Module """
>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
from models.base_model import BaseModel


class City(BaseModel):
<<<<<<< HEAD
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
=======
    """ The city class """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """the city class constructor"""
        super().__init__(*args, **kwargs)
>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
