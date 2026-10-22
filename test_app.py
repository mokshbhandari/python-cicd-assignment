
import unittest
from app import add_numbers


class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(10, 20), 30)

    def test_add_zero(self):
        self.assertEqual(add_numbers(5, 0), 5)

    def test_add_negative_number(self):
        self.assertEqual(add_numbers(-5, 2), -3)


if __name__ == "__main__":
    unittest.main()
