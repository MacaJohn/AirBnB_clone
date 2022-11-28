#!/usr/bin/env python3
""" holds class User """
from models.base_model import BaseModel


class User(BaseModel):
    """Representation of a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """constructor of the User class"""
        super().__init__(*args, **kwargs)
