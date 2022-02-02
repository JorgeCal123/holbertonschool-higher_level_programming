#!/usr/bin/python3
"""class Student"""


class Student:
    """ Student class"""

    def __init__(self, first_name, last_name, age):
        """method constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        student = {}
        a = vars(self)
        if attrs is None:
            return a
        for key, val in a.items():
            if key in attrs:
                student[key] = val
        return student
