#!/usr/bin/python3
"""Module for a rectangle class"""


class Rectangle:
    """This class defines a simple Rectangle."""

    number_of_instances = 0
    """int: The number of active instances."""

    print_symbol = '#'
    """type: Print symbol, can be any type."""

    Args:
        width: The width of rectangle.
        height: The height of rectangle
    """
    self.width = width
    self.height = height
    Rectangle.number_of_instances += 1
    """

@property
def width(self):
    """Property for the width of the rectangle.

    Raises:
        TypeError: if width is not an integer.
        ValueError: if the width is not less than 0.
    """
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
    """Property for the height of the rectangle.

    Raises:
        TypeError: if height is not an integer.
        ValueError: if the height is not less than 0.
    """
    return self.__height

@height.setter
def height(self, value):
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value

def perimeter(self):
    """Returns perimeter of the rectangle."""
    if not self.width * self.height:
        return 0
    return (self.width + self.height) * 2

def __str__(self):
    """Returns formal string represantation..."""
    if not self.width or not self.height:
        return ""
    return ((str(self.print_symbol) * self.width + "\n") *
            self.height) [:-1]

def __repr__(self):
    """Returns formal string represantation..."""
    return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

def __del__(self):
    """called at instance deletion."""
    print("Bye rectangle...")
    Rectangle.number_of_instances -= 1

@staticmethod
def bigger_or_equal(rect_1, rect_2):
    """Returns the bigger of two rectangles.

    Args:
        rect_1: The first rectangle.
        rect_2: The second rectangle.
    Raises:
        TypeError: If rect_1, rect_2 are not instances of Rectangle
    Returns:
        The rectangle with the larger area.
    """
    if not isinstance(rect_1, Rectangle):
        raise TypeError("rect_1 must be an instance of Rectangle")
    if not isinstance(rect_1, Rectangle):
        raise TypeError("rect_2 must be an instance of Rectangle")
    if rect_2.area() > rect_!.area():
        return rect_2
    return rect_1

