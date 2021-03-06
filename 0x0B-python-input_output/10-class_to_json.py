#!/usr/bin/python3

"""
This is a module for class_to_json.
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object:"""
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    if hasattr(obj, "__slots__"):
        return obj.__slots__
