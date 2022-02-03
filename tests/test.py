"""
Sample file illustrating the basics of testing with Python.

author: @arjunsavel
"""

import unittest
from src.template.fit_line import *


class TestFuncs(unittest.TestCase):

    # def example_test(self):
    # in rough order of usefulness, these are some assert statements!
    # self.assertEqual(A, B) # asserts that floats or ints A, B are equal
    # self.assertNotEqual(A, B) # asserts that floats or ints A, B are not equal
    # self.assertTrue(A) # asserts that A is True
    # self.assertFalse(A) # asserts that A is False
    # self.assertCountEqual(A, B) # asserts that arrays A and B are element-wise equal
    # self.assertIn(A, B) # asserts that A in B
    # self.assertNotIn(A, B) # asserts that A not in B
    # self.assertIs(A, B) # asserts that A is B
    # self.assertIsNot(A, B) # asserts that A is not B
    # self.assertIsInstance(A, B) # asserts that A is an instance of B
    # self.assertNotIsInstance(A, B) # asserts that A is not an instance of B
    # self.assertRaises(A) # asserts that error A is raised

    def test_exponential_base_1_power_2(self):
        base = 1
        power = 2
        result = exp_func(base, power)
        expected_result = 1
        self.assertEqual(result, expected_result)

    def test_exponential_new(self):
        # WRITE your test here!
        # CHANGE the below assert statement
        self.assertTrue(True)
