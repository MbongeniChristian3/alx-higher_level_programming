#!/usr/bin/python3
"""Defining from_json_string function."""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text fie"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)

