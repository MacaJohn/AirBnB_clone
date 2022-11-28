#!/usr/bin/env python3
""" City class Module """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """the city class constructor"""
        super().__init__(*args, **kwargs)
