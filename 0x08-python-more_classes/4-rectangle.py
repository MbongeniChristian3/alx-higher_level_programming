#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
            """returns the area of the rectangle"""
            return self.__width * self.__height

    def perimeter(self):
            """returns the perimeter of the rectangle"""
            if self.__width == 0 or self.__height == 0:
                return 0
            return (self__width * 2) + (self.__height * 2)

    def __str__(self):
            """returns printable string represantation of the rectagle"""
            string = ""
            if self.__width != 0  and self.__height != 0:
                string += "\n".join("#" * self.__width
                                    for j in range(self.__height))
            return string

    def __repr__(self):
            """returns a string represantation of the rectangle for reproduction"""
            return "Rectangle({:D}, {:d})".format(self.__width, self.__height)



