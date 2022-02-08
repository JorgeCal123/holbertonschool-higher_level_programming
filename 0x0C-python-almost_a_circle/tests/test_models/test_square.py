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

    def test_set_size(self):
        square2 = Square(15)
        square2.size = 10
        self.assertEqual(square2.size, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square2.size = "10"

    def test_update_case1(self):
        square3 = Square(15)
        square3.update(1, 2, 3, 4)
        self.assertEqual(square3.id, 1)
        self.assertEqual(square3.size, 2)
        self.assertEqual(square3.x, 3)
        self.assertEqual(square3.y, 4)

    def test_update_case2(self):
        square3 = Square(15)
        square3.update(size=7, id=89, y=1, x=3)
        self.assertEqual(square3.id, 89)
        self.assertEqual(square3.size, 7)
        self.assertEqual(square3.x, 3)
        self.assertEqual(square3.y, 1)

    def test_to_dictionary(self):
        square4 = Square(10, 2, 1)
        self.assertDictEqual(square4.to_dictionary(), {'id': 3, 'x': 2, 'size': 10, 'y': 1})

if __name__ == "__main__":
    unittest.main()

