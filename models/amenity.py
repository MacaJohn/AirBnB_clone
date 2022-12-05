<<<<<<< HEAD
#!/usr/bin/python3
""" State Module for HBNB project """
=======
#!/usr/bin/env python3
""" The module of amenity class """
>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
from models.base_model import BaseModel


class Amenity(BaseModel):
<<<<<<< HEAD
    name = ""
=======
    """Representation of Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """ The constructor of the Amenity class """
        super().__init__(*args, **kwargs)
>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
