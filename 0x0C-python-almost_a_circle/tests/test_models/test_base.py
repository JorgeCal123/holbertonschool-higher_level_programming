#!/usr/bin/python3

"""Unittest classes"""
import unittest
from models.base import Base


class TestSquare(unittest.TestCase):
    """TestSquare"""

    def test_base(self):
        base1 = Base(10)
        self.assertIsInstance(base1, Base)
        self.assertEqual(base1.id, 10)

if __name__ == "__main__":
    unittest.main()
