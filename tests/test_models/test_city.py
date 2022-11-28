#!/usr/bin/python3
""" Contains the Tests for City class """
from datetime import datetime
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Test class for City"""
    def test_city_class_and_attributes(self):
        """Test that City is a subclass of BaseModel"""
        city = City()

        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_city_to_dict(self):
        """
            Test the city.to_dict() method
        """
        city = City()
        c_dict = city.to_dict()
        self.assertEqual(type(c_dict), dict)
        self.assertTrue("__class__" in c_dict)

    def test_city_to_dict_values(self):
        """
            Test the values returned from to_dict method
        """
        city = City()
        c_dict = city.to_dict()
        self.assertEqual(c_dict["__class__"], "City")
        self.assertEqual(type(c_dict["updated_at"]), str)
        self.assertEqual(c_dict["created_at"], city.created_at.isoformat())

    def test_city_to_str(self):
        """
            Test that the str method has the correct output
        """
        city = City()
        strng = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(strng, str(city))
