#!/usr/bin/python3
""" Contains the Tests for State class """
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Test class for State"""
    def test_state_class_and_attributes(self):
        """Test that Amenity is a subclass of BaseModel"""
        state = State()

        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_state_to_dict(self):
        """
            Test the state.to_dict() method
        """
        state = State()
        s_dict = state.to_dict()
        self.assertEqual(type(s_dict), dict)
        self.assertTrue("__class__" in s_dict)

    def test_state_to_dict_values(self):
        """
            Test the values returned from to_dict method
        """
        state = State()
        s_dict = state.to_dict()
        self.assertEqual(s_dict["__class__"], "State")
        self.assertEqual(type(s_dict["updated_at"]), str)
        self.assertEqual(s_dict["created_at"], state.created_at.isoformat())

    def test_state_to_str(self):
        """
            Test that the str method has the correct output
        """
        state = State()
        strng = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(strng, str(state))
