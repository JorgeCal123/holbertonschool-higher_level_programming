#!/usr/bin/python3
"""Class Base"""
import json


class Base:
    """Class father"""

    __nb_objects = 0

    def __init__(self, id=None):
        """method constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """method to_json_string"""
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)
