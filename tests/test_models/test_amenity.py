#!/usr/bin/python3
"""Unittests for the Amenity class."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Unittests for the Amenity class."""

    def test_is_subclass_of_basemodel(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_name_is_public_str(self):
        self.assertEqual(str, type(Amenity.name))


if __name__ == "__main__":
    unittest.main()
