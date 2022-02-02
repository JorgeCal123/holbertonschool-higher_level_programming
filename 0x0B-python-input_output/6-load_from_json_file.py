#!/usr/bin/python3
"""load_from_json_file"""
import json


def load_from_json_file(filename):
    """ function that creates an Object from a JSON file"""
    with open(filename, 'rt') as f:
        return json.load(f)
