#!/usr/bin/python3
"""Defines a locked class."""


class lockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but atttributes called 'first_name'.
    """

    __slots__ = ["first_name"]
