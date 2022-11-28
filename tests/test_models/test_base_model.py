#!/usr/bin/env python3
"""
    This module contains test suites,
    cases and models for the base_model class
"""

import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ test suites for testing the an object of BaseModel """

    def setUp(self):
        """ set up method to factor out repeatitive codes """
        self.basemodel = BaseModel()
        self.basemodel_1 = BaseModel()

    def test_base_model_id(self):
        """ test base_model.id attribute
            Add a test for base_model.id using regex
        """
        self.assertIs(type(self.basemodel.id), str)
        self.assertIs(type(self.basemodel_1.id), str)
        self.assertEqual(len(self.basemodel.id), 36)
        self.assertEqual(len(self.basemodel_1.id), 36)

    def test_basemodel_created_at_and_updated_at(self):
        """
            tests the attributes
            basemodel.created_at
            basemodel.updated_at
        """
        self.assertIs(type(self.basemodel.created_at), datetime)
        self.assertIs(type(self.basemodel_1.created_at), datetime)

        self.assertIs(type(self.basemodel.updated_at), datetime)
        self.assertIs(type(self.basemodel_1.updated_at), datetime)

        self.assertEqual(self.basemodel.created_at, self.basemodel.updated_at)
        self.assertEqual(
                self.basemodel_1.created_at, self.basemodel_1.updated_at)

    def test_basemodel_created_at_and_updated_at_after_save(self):
        """
            tests the the following attributes after calling basemodel.save()
            basemodel.created_at
            basemodel.updated_at
        """
        self.basemodel.save()
        self.basemodel_1.save()

        self.assertIs(type(self.basemodel.updated_at), datetime)
        self.assertIs(type(self.basemodel_1.updated_at), datetime)

        self.assertNotEqual(
                self.basemodel.created_at, self.basemodel.updated_at)
        self.assertNotEqual(
                self.basemodel_1.created_at, self.basemodel_1.updated_at)

    def test_basemodel_str(self):
        """
            tests the basemodel.str attribute
        """
        bm_name = self.basemodel.__class__.__name__
        bm_id = self.basemodel.id
        bm_id_1 = self.basemodel_1.id
        bm_name_1 = self.basemodel_1.__class__.__name__
        bm_dict = self.basemodel.__dict__
        bm_dict_1 = self.basemodel_1.__dict__

        base_model_str = '[{}] ({}) {}'.format(bm_name, bm_id, bm_dict)
        base_model_1_str = '[{}] ({}) {}'.format(
                bm_name_1, bm_id_1, bm_dict_1)

        self.assertIs(type(str(self.basemodel)), str)
        self.assertIs(type(str(self.basemodel_1)), str)
        self.assertEqual(str(self.basemodel), base_model_str)
        self.assertEqual(str(self.basemodel_1), base_model_1_str)

    def test_basemodel_to_dict(self):
        """
            tests the basemodel.to_dict() method
        """
        self.basemodel.name = "undelund"
        self.basemodel_1.name = "undeberge"
        self.basemodel.my_number = 89
        self.basemodel_1.my_number = 90

        bm_dict = self.basemodel.to_dict()
        bm_dict_1 = self.basemodel.to_dict()

        self.assertEqual(
                bm_dict['__class__'], self.basemodel.__class__.__name__)
        self.assertEqual(bm_dict['name'], self.basemodel.name)
        self.assertEqual(bm_dict['my_number'], self.basemodel.my_number)
        self.assertEqual(
                bm_dict['updated_at'], self.basemodel.updated_at.isoformat())
        self.assertIs(
                type(datetime.fromisoformat(bm_dict['updated_at'])), datetime)
        self.assertEqual(
                datetime.fromisoformat(
                    bm_dict['created_at']), self.basemodel.created_at)
        self.assertIs(
                type(datetime.fromisoformat(
                    bm_dict_1['updated_at'])), datetime)
        self.assertIs(type(bm_dict['id']), str)
        self.assertEqual(bm_dict['id'], self.basemodel.id)

        def test_init_with_kwarg_variable(self):
            """ tests the BaseModel __init__(**kwargs) """
            basemodel = BaseModel()
            basemodel.name = 'My second Model'
            basemodel.my_number = 91
            bm_dict = basemodel.to_dict()

            basemodel_1 = BaseModel(**bm_dict)
            bm_dict_1 = basemodel_1.to_dict()

            empty_dict = {}
            rand_dict_1 = {
                            id: str(uuid.uuid4()),
                            __class__: 'BaseModel',
                            name: 'second to the last',
                            my_number: 92,
                            created_at: datetime.isoformat(datetime.now())
            }
            rand_tuple_1 = ()

            basemodel_2 = BaseModel(**rand_dict_1)
            bm_dict_2 = basemodel_2.to_dict()

            self.assertEqual(bm_dict, bm_dict_1)
            self.assertIsNot(bm_dict, bm_dict_1)
            self.assertNotEqual(basemodel, basemodel_1)
            self.assertIsNot(basemodel, basemodel_1)
            self.assertEqual(rand_dict_1, bm_dict_2)
            self.assertIsNot(rand_dict_1, bm_dict_2)

            basemodel_3 = BaseModel(**empty_dict)
            with self.assertRaises(AttributeError, basemodel_3.name):
                """Raises an AttributeError if basemodel_3.name is called """
                raise AttributeError

            with self.assertRaises(AttributeError, basemodel_3.my_number):
                """
                    Raises an AttributeError if basemodel_3.my_number is called
                """
                raise AttributeError

        def test_kwargs_is_empty(self):
            """
                checks that id, created_at and updated_at are generated even
                when kwargs is empty
            """
            my_dict = {}
            b = BaseModel(**my_dict)
            self.assertTrue(type(b.id) is str)
            self.assertTrue(type(b.created_at) is datetime)
            self.assertTrue(type(b.updated_at) is datetime)

        def test_kwargs_not_empty(self):
            """
                checks that id, created_at and updated_at are created
                from kwargs
            """
            my_dict = {
                        "id": uuid4(),
                        "created_at": datetime.utcnow().isoformat(),
                        "updated_at": datetime.now().isoformat()
                        }
            b = BaseModel(**my_dict)
            self.assertEqual(b.id, my_dict["id"])
            self.assertEqual(b.created_at,
                             datetime.strptime(my_dict["created_at"],
                                               "%Y-%m-%dT%H:%M:%S.%f"))
            self.assertEqual(b.updated_at,
                             datetime.strptime(my_dict["updated_at"],
                                               "%Y-%m-%dT%H:%M:%S.%f"))

        def test_save_method_update_file(self):
            """
                Tests that save method updates file
            """
            b = BaseModel()
            b.save()
            bid = "BaseModel.{}".format(b.id)
            with open("file.json", encoding="utf-8") as f:
                self.assertIn(bid, f.read())


if __name__ == '__main__':
    unittest.main()
