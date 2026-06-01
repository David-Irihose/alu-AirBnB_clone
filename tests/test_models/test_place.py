#!/usr/bin/python3
"""Unittests for the Place class."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Unittests for the Place class."""

    def test_is_subclass_of_basemodel(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_city_id_is_public_str(self):
        self.assertEqual(str, type(Place.city_id))

    def test_number_rooms_is_public_int(self):
        self.assertEqual(int, type(Place.number_rooms))

    def test_latitude_is_public_float(self):
        self.assertEqual(float, type(Place.latitude))

    def test_amenity_ids_is_public_list(self):
        self.assertEqual(list, type(Place.amenity_ids))


if __name__ == "__main__":
    unittest.main()
