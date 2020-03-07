import unittest
from src.math import Math


class MathTest(unittest.TestCase):
    def test_addition(self):
        # Make tests fail
        self.assertEqual(Math.addition(3, 4), 8)

    def test_addition_duplicate(self):
        self.assertEqual(Math.addition(4, 5), 10)


