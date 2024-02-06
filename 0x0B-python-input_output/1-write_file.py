#!/usr/bin/python3
"""Defining write_file with two arguments."""


def write_file(filename="", text=""):
    """reads filename eith utf-8"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
