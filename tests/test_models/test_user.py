#!/usr/bin/python3
"""Unittests for the User class."""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unittests for the User class."""

    def test_is_subclass_of_basemodel(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_default_attributes_empty(self):
        u = User()
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")


if __name__ == "__main__":
    unittest.main()
