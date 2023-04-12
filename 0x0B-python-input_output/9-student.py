#!/usr/bin/python3
""" Deffines a class Student
"""

class Student:
    """ Initialises student.
    Args:
         first_name (str): first name of a student
         last_name (str): last name of the student
         age (int): the students age
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

    def to_json(self):
        """get a dictionary rep of the student"""
        return self.__dict__
