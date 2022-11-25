#!/usr/bin/env python3
""" This module contains test suites, cases and models for the base_model class"""

import unittest
import uuid
import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ test suites for testing the an object of BaseModel """

    def setUp(self):
        self.basemodel = BaseModel()
        self.basemodel_1 = BaseModel()

    def test_base_model_id(self):
        self.assertIs(type(self.basemodel.id), str)
        self.assertIs(type(self.basemodel_1.id), str)
        self.assertEqual(len(self.basemodel.id), 36)
        self.assertEqual(len(self.basemodel_1.id), 36)

    def test_basemodel_created_at_and_updated_at(self):
        self.assertIs(type(self.basemodel.created_at), datetime.datetime)
        self.assertIs(type(self.basemodel_1.created_at), datetime.datetime)

        self.assertIs(type(self.basemodel.updated_at), datetime.datetime)
        self.assertIs(type(self.basemodel_1.updated_at), datetime.datetime)

        self.assertEqual(self.basemodel.created_at, self.basemodel.updated_at)
        self.assertEqual(self.basemodel_1.created_at, self.basemodel_1.updated_at)

    def test_basemodel_created_at_and_updated_at_after_save(self):
        self.basemodel.save()
        self.basemodel_1.save()

        self.assertIs(type(self.basemodel.updated_at), datetime.datetime)
        self.assertIs(type(self.basemodel_1.updated_at), datetime.datetime)

        self.assertNotEqual(self.basemodel.created_at, self.basemodel.updated_at)
        self.assertNotEqual(self.basemodel_1.created_at, self.basemodel_1.updated_at)

    def test_basemodel_str(self):
        bm_name = self.basemodel.__class__.__name__
        bm_id = self.basemodel.id
        bm_id_1 = self.basemodel_1.id
        bm_name_1 = self.basemodel_1.__class__.__name__
        bm_dict = self.basemodel.__dict__
        bm_dict_1 = self.basemodel_1.__dict__

        base_model_str = '[{}] ({}) {}'.format(bm_name, bm_id, bm_dict)
        base_model_1_str = '[{}] ({}) {}'.format(bm_name_1, bm_id_1, bm_dict_1)

        self.assertIs(type(str(self.basemodel)), str)
        self.assertIs(type(str(self.basemodel_1)), str)
        self.assertEqual(str(self.basemodel), base_model_str)
        self.assertEqual(str(self.basemodel_1), base_model_1_str)

    def test_basemodel_to_dict(self):
        self.basemodel.name = "undelund"
        self.basemodel_1.name = "undeberge"
        self.basemodel.my_number = 89
        self.basemodel_1.my_number = 90

        bm_dict = self.basemodel.to_dict()
        bm_dict_1 = self.basemodel.to_dict()

        self.assertEqual(bm_dict['__class__'], self.basemodel.__class__.__name__)
        self.assertEqual(bm_dict['name'], self.basemodel.name)
        self.assertEqual(bm_dict['my_number'], self.basemodel.my_number)
        self.assertEqual(bm_dict['updated_at'], self.basemodel.updated_at.isoformat())
        self.assertIs(type(datetime.datetime.fromisoformat(bm_dict['updated_at'])), datetime.datetime)
        self.assertEqual(datetime.datetime.fromisoformat(bm_dict['created_at']), self.basemodel.created_at)
        self.assertIs(type(datetime.datetime.fromisoformat(bm_dict_1['updated_at'])), datetime.datetime)
        self.assertIs(type(bm_dict['id']), str)
        self.assertEqual(bm_dict['id'], self.basemodel.id)

if __name__ == '__main__':
    unittest.main()
