#!/usr/bin/python3
"""Unittests for the Review class."""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Unittests for the Review class."""

    def test_is_subclass_of_basemodel(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_place_id_is_public_str(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id_is_public_str(self):
        self.assertEqual(str, type(Review.user_id))

    def test_text_is_public_str(self):
        self.assertEqual(str, type(Review.text))


if __name__ == "__main__":
    unittest.main()
