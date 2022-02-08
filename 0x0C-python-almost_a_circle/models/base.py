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
        dic = []
        if list_objs:
            for i in list_objs:
                dic.append(cls.to_dictionary(i))
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        "metohd from_json_string"
        if json_string is None or len(json_string) == 0:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """method create"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
