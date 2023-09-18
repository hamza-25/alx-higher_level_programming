#!/usr/bin/python3
"""define unittest for base.py"""
import unittest
from models.base import Base

class Base_instantiation_test(unittest.TestCase):
    """testing instantiation of the Base class."""

    def test_no_arg(self):
        ob1 = Base()
        ob2 = Base()
        self.assertEqual(ob1.id, ob2.id - 1)

if __name__ == "__main__":
    unittest.main()
