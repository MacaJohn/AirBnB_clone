#!/usr/bin/python3
""" Contains the Tests for Review class """
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Test class for Review"""
    def test_review_class_and_attributes(self):
        """Test that Review is a subclass of BaseModel"""
        review = Review()

        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertTrue(hasattr(review, "text"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_to_dict(self):
        """
            Test the review.to_dict() method
        """
        review = Review()
        r_dict = review.to_dict()
        self.assertEqual(type(r_dict), dict)
        self.assertTrue("__class__" in r_dict)

    def test_review_to_dict_values(self):
        """
            Test the values returned from to_dict method
        """
        review = Review()
        r_dict = review.to_dict()
        self.assertEqual(r_dict["__class__"], "Review")
        self.assertEqual(type(r_dict["updated_at"]), str)
        self.assertEqual(r_dict["created_at"], review.created_at.isoformat())

    def test_review_to_str(self):
        """
            Test that the str method has the correct output
        """
        review = Review()
        strng = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(strng, str(review))
