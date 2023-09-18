#!/usr/bin/python3
"""defines a base class"""


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
