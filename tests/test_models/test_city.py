#!/usr/bin/python3
"""Unittests for the City class."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Unittests for the City class."""

    def test_is_subclass_of_basemodel(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_state_id_is_public_str(self):
        self.assertEqual(str, type(City.state_id))

    def test_name_is_public_str(self):
        self.assertEqual(str, type(City.name))


if __name__ == "__main__":
    unittest.main()
