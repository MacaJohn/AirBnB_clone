<<<<<<< HEAD
#!/usr/bin/python3
""" Place Module for HBNB project """
=======
#!/usr/bin/env python3
""" holds class Place """
>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
from models.base_model import BaseModel


class Place(BaseModel):
<<<<<<< HEAD
    """ A place to stay """
=======
    """ Representation of Place """
>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
<<<<<<< HEAD
=======

    def __init__(self, *args, **kwargs):
        """constructor of the place class"""
        super().__init__(*args, **kwargs)
>>>>>>> f3205f486e56f35831bb666b1beee4a86f9b2fcb
