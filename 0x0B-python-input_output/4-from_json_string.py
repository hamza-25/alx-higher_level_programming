#!/usr/bin/python3
"""Defines a JSON-to-object."""
import json


def from_json_string(my_str):
    """Python object representation"""
    return json.loads(my_str)
