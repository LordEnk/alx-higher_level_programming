#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""
     def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return int(self) != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return int(self) == other
