#!/usr/bin/python3
"""Defines a JSON file-reading."""
import json


def load_from_json_file(filename):
    """create Python object from a json file.
    """
    with open(filename):
        return json.load(open(filename))
