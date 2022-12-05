#!/usr/bin/python3
""" Contains the Tests for Amenity class """
from datetime import datetime
from models import amenity
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Test class for Amenity"""
    def test_amenity_class_and_attributes(self):
        """Test that Amenity is a subclass of BaseModel"""
        amenity = Amenity()

        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_amenity_to_dict(self):
        """
            Test the amenity.to_dict() method
        """
        amenity = Amenity()
        a_dict = amenity.to_dict()
        self.assertEqual(type(a_dict), dict)
        self.assertTrue("__class__" in a_dict)

    def test_amenity_to_dict_values(self):
        """
            Test the values returned from to_dict method
        """
        amenity = Amenity()
        a_dict = amenity.to_dict()
        self.assertEqual(a_dict["__class__"], "Amenity")
        self.assertEqual(type(a_dict["updated_at"]), str)
        self.assertEqual(a_dict["created_at"], amenity.created_at.isoformat())

    def test_str(self):
        """
            Test that the str method has the correct output
        """
        amenity = Amenity()
        strng = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(strng, str(amenity))
