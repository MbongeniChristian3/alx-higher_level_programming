#!/usr/bin/python3
"""Defining to_json_string function."""


import json


def to_json_string(my_obj):
    """returns json represantation of an object"""
    return json.dumps(my_obj)
