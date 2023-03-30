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
