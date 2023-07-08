#!/usr/bin/python3
"""Unittest module for User"""


import unittest
from datetime import datetime

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Unittest for the User class"""

    def test_attributes(self):
        user = User()
        user.email = "rick.sanchez@mail.com"
        user.first_name = "Rick"
        user.last_name = "Sanchez"
        user.password = "pickle"

        self.assertEqual(user.email, "rick.sanchez@mail.com")
        self.assertEqual(user.first_name, "Rick")
        self.assertEqual(user.last_name, "Sanchez")
        self.assertEqual(user.password, "pickle")

    def test_attributes_types(self):
        self.assertEqual(str, type(User.email))
        self.assertEqual(str, type(User.first_name))
        self.assertEqual(str, type(User.last_name))
        self.assertEqual(str, type(User.password))

    def test_subclass(self):
        self.assertTrue(issubclass(User, BaseModel))


    if __name__ == '__main__':
        unittest.main()
