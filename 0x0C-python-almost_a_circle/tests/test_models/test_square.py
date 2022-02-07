#!/usr/bin/python3
"""method square"""

import unittest
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):
    

    def test_base(self):
        square1 = Square(10)
        self.assertIsInstance(square1, Base)
        self.assertIsInstance(square1, Square)
        self.assertEqual(square1.id, 1)
