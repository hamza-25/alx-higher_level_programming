#!/usr/bin/python3
"""define rectangle file testing"""
from models.rectangle import Rectangle

import unittest

class TestCaseRectangleClass(unittest.TestCase):
    def print_width_height_rectangle(self):
        obj1 = Rectangle(10, 5)
        self.assertEqual(obj1.width, 10)
        self.assertEqual(obj1.height, 5)

if __name__ == "__main__":
    unittest.main()
