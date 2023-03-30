#!/usr/bin/python3
"""
defines a square
"""

class Square:
    """representsthe square sides"""
    def __init__(self, size=0):
        self.size = size

        @property
        def size(self):
            """gets the private instance size"""
            return self.__size

        @size.setter
        def size(self, value):
            """setter for the private instance size"""
            if not instance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size  = value

        def area(self):
            """gets the area of this square"""
            return self.size * self.size
