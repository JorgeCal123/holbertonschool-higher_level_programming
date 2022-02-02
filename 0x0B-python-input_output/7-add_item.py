#!/usr/bin/python3
"""add_item"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    loadFile = load_from_json_file("add_item.json")
except FileNotFoundError:
    loadFile = []

argc = len(sys.argv)
for i in range(1, argc):
    loadFile.append(sys.argv[i])
save_to_json_file(loadFile, "add_item.json")
