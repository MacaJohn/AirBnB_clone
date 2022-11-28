#!/usr/bin/env python3
""" The module of the state class """
from models.base_model import BaseModel


class State(BaseModel):
    """Representation of state """
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor of the state class"""
        super().__init__(*args, **kwargs)
