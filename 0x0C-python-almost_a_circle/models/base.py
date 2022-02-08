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

    @staticmethod
    def to_json_string(list_dictionaries):
        """method to_json_string"""
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        "method save_to_file"
        file_JSON = []
        if list_objs is None:
            return file_JSON
        else:
            for i in list_objs:
                file_JSON.append(cls.to_dictionary(i))
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(file_JSON))
