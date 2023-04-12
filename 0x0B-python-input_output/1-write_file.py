#!/usr/bin/python3
"""This module defines a file-writing function.
"""

def write_file(filename="", text=""):
    """ writes a string to a UTB8 file """
    with open(filename, "w", encoding="ytf-8") as f:
        return f.write(text)
