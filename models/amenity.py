#!/usr/bin/env python3
""" The module of amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representation of Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """ The constructor of the Amenity class """
        super().__init__(*args, **kwargs)
