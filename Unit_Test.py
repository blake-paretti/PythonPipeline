import unittest

from operations import add, sub, mult, div


class TestSum(unittest.TestCase):

    def test_add_operation_returns_correct_value(self):
        self.assertEqual(add(10, 90), 100)
        
    def test_substract_operation_returns_correct_value(self):
        self.assertEqual(subtract(100, 90), 10)

    def test_multiply_operation_returns_incorrect_value(self):
        self.assertEqual(multiply(10, 10), 100)

    def test_division_operation_returns_incorrect_value(self):
        self.assertEqual(divide(100, 10), 10)


TestSum()