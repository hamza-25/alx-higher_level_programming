#!/usr/bin/python3
"""Defines a JSON file-writing."""
import json


def save_to_json_file(my_obj, filename):
    """JSON representation save_to_json_file."""
    with open(filename, "w"):
        json.dump(my_obj, open(filename, "w"))
