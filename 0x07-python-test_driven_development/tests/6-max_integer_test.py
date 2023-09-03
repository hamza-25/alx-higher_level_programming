#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest


max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class TestMaxInteger inhert TestCase.
    """

    
    def test_get_max_value(self):
        """funcion test_get_max_value that test mult case of list.
        """
        self.assertEqual(max_integer([100, 45, 52, 101]), 101)
        self.assertEqual(max_integer([5,5,5,5]), 5)
        self.assertEqual(max_integer([-1,7,4,10]), 10)
        self.assertEqual(max_integer([-10,-1,-70,-5]), -1)
        self.assertEqual(max_integer([101, 45, 52, -101]), 101)
        self.assertEqual(max_integer([54]), 54)
        self.assertEqual(max_integer(list(range(20))), 19)
        self.assertEqual(max_integer([101, 52, 4,52, 4, 101, 4]), 101)
    def test_input_empty_list(self):
        """function that test with empty list.
        """
        self.assertEqual(max_integer([]), None)
if __name__ == "__main__":
    unittest.main()
