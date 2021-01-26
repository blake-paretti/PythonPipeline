import unittest

from operations import add, sub, mult, div


class TestSum(unittest.TestCase):

    def test_add_operation_returns_correct_value(self):
        self.assertEqual(add(10, 90), 100)
        
    def test_substract_operation_returns_correct_value(self):
        self.assertEqual(sub(100, 90), 10)

    def test_multiply_operation_returns_incorrect_value(self):
        self.assertEqual(mult(10, 10), 100)

    def test_division_operation_returns_incorrect_value(self):
        self.assertEqual(div(100, 10), 10)


if __name__ == '__main__':
    unittest.main()
