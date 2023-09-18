#!/usr/bin/python3
"""define rectangle file testing"""

import unittest
from models.rectangle import Rectangle


class Rectangle_instantiation_test(unittest.TestCase):
    """testing instantiation of Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

if __name__ == "__main__":
    unittest.main()
