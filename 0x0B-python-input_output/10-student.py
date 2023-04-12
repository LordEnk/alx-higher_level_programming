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

    def to_json(self, attrs-None):
        """get a dictionary rep of the student
        if attrs is a list of strings only attribute names mux=st be retrieved
        else all sttributes must be retrieved
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
