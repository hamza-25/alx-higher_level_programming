#!/usr/bin/python3
"""define unittest for base.py"""
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):

    def test_same_id(self):
        obj1 = Base()
        #obj2 = Base(1)
        self.assertEqual(print(obj1.id), 1)
        #self.assertEqual(print(obj1.id), 2)

if __name__ == "__main__":
    unittest.main()
