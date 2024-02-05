#!/usr/bin/python3
"""Defines an inherited list class Mylist."""

class MyList(list):
    """lmplements sorted printing for the built-in class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))

