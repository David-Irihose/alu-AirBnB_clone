#!/usr/bin/python3
"""Unittests for the State class."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Unittests for the State class."""

    def test_is_subclass_of_basemodel(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_name_is_public_str(self):
        self.assertEqual(str, type(State.name))

    def test_default_name_empty(self):
        self.assertEqual(State().name, "")


if __name__ == "__main__":
    unittest.main()
