#!/usr/bin/python3
"""defines a base class"""
import json


class Base:
    """representation of class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize base class"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string"""
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file_json:
            if list_objs is None:
                file_json.write("[]")
            else:
                list_dicts = []
                for obj in list_objs:
                    list_dicts.append(obj.to_dictionary())
                file_json.write(Base.to_json_string(list_dicts))
