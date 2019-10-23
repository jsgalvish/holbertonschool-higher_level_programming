#!/usr/bin/python3

""" base class """

import json
import os.path

class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return JSON """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list")
        if any(type(x) != dict for x in list_dictionaries):
            raise TypeError("list_dictionaries must contain dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save JSON  file """
        if type(list_objs) != list and list_objs is not None:
            raise TypeError("list_objs must be a list")
        if list_objs is None or list_objs == []:
            output = []
        else:
            first = type(list_objs[0])
            if any(type(x) != first for x in list_objs):
                raise ValueError("all elements of list_objs must match")
            output = [c.to_dictionary() for c in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(output))

    @staticmethod
    def from_json_string(json_string):
        """ JSON to string """
        if json_string is None or json_string == "":
            return []
        if type(json_string) != str:
            raise TypeError("json_string must be a string")
        loads = json.loads(json_string)
        for d in loads:
            if type(d) != dict:
                raise ValueError("json_string must contain dictionaries")
        return loads

    @classmethod
    def create(cls, **dictionary):
        """ create instance """
        test = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        test.update(**dictionary)
        return test

    @classmethod
    def load_from_file(cls):
        """ load instances """
        filename = str(cls).split(".")[-1][:-2] + ".json"
        if not os.path.exists(filename):
            return []
        res = []
        with open(filename, "r") as f:
            dicts = cls.from_json_string(f.readline())
        for d in dicts:
            res.append(cls.create(**d))
        return res
