#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest


max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_get_max_value(self):
        list_num = [100, 45, 52, 101]
        self.assertEqual(max_integer(list_num), 101)
    def test_input_empty_list(self):
        self.assertEqual(max_integer([]), None)
if __name__ == "__main__":
    unittest.main()
