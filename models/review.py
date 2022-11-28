#!/usr/bin/env python3
""" Review class Module """
from models.base_model import BaseModel


class Review(BaseModel):
    """ The Review class """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ The review class constructor """
        super().__init__(*args, **kwargs)
