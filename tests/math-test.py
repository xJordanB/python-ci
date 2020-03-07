import unittest
from src.math import Math


class MathTest(unittest.TestCase):
    def test_addition(self):
        # Make tests fail
        self.assertEqual(Math.addition(3, 4), 8)
