#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check
        a_class (type): The class to match the type of the obj to
    Returns:
        If obj is inherited instance of a_class - True.
        Otherwise _ False.
        """
        if issubclass(type(obj), a_class) and type(obj) != a_class:
            return True
        return False
