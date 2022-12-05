#!/usr/bin/python3
""" Contains the Tests for Place class """
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Test class for Place"""
    def test_place_class_and_attributes(self):
        """Test that Place is a subclass of BaseModel"""
        place = Place()

        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertIs(type(place.amenity_ids), list)

    def test_place_to_dict(self):
        """
            Test the city.to_dict() method
        """
        place = Place()
        p_dict = place.to_dict()
        self.assertEqual(type(p_dict), dict)
        self.assertTrue("__class__" in p_dict)

    def test_city_to_dict_values(self):
        """
            Test the values returned from to_dict method
        """
        place = Place()
        p_dict = place.to_dict()
        self.assertEqual(p_dict["__class__"], "Place")
        self.assertEqual(type(p_dict["updated_at"]), str)
        self.assertEqual(p_dict["created_at"], place.created_at.isoformat())

    def test_place_to_str(self):
        """
            Test that the str method has the correct output
        """
        place = Place()
        strng = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(strng, str(place))
