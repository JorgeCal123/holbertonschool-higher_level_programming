#!/usr/bin/python3
"""Unittest class Rectangle"""

import unittest
import io
from contextlib import redirect_stdout

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """TestRectangle"""
    
    rectangle4 = Rectangle(10, 2)

    def test_insert_value_case_1(self):
        rectangle1 = Rectangle(10, 2)
        self.assertEqual(rectangle1.width, 10)
        self.assertEqual(rectangle1.height, 2)
        self.assertEqual(rectangle1.x, 0)
        self.assertEqual(rectangle1.y, 0)

    def test_insert_value_case_2(self):
        rectangle2 = Rectangle(10, 2, 4, 3)
        self.assertEqual(rectangle2.width, 10)
        self.assertEqual(rectangle2.height, 2)
        self.assertEqual(rectangle2.x, 4)
        self.assertEqual(rectangle2.y, 3)

    def test_insert_value_case_3(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle3 = Rectangle("10", 2, 4, 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle3 = Rectangle(10, "2", 4, 3)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle3 = Rectangle(10, 2, "4", 3)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rectangle3 = Rectangle(10, 2, 4, "3")

    def test_insert_value_case_4(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle4 = Rectangle(-5, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle4 = Rectangle(0, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle4 = Rectangle(5, -4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle4 = Rectangle(5, 0)

    def test_insert_value_case_5(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rectangle4 = Rectangle(5, 4, -3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rectangle4 = Rectangle(5, 4, 3, -6)

    def test_calculate_area_case_1(self):
        rectangle5 = Rectangle(3, 2)
        self.assertEqual(rectangle5.area(), 6)

    def test_display_case_1(self):
        rectangle6 = Rectangle(2, 2)
        with io.StringIO() as buf, redirect_stdout(buf):
            rectangle6.display()
            output = buf.getvalue()
        self.assertEqual(output, '##\n##\n')

    def test_display_case_2(self):
        rectangle7 = Rectangle(2, 3, 1, 4)
        with io.StringIO() as buf, redirect_stdout(buf):
            rectangle7.display()
            output = buf.getvalue()
        self.assertEqual(output, '\n\n\n\n ##\n ##\n ##\n')

    def test_str_case_1(self):
        rectangle6 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(Rectangle.__str__(rectangle6), "[Rectangle] (12) 2/1 - 4/6")

if __name__ == "__main__":
    unittest.main()
