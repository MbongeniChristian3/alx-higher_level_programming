#!/usr/bin/python3
"""Defines a class checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check
        a_class (type): The class to match the type of the objto
    Returns:
        If obj is exactly an instance of a-class - True
        Otherwise _ False.
        """
        if isinstance(obj, a_class):
            return True
        return False

