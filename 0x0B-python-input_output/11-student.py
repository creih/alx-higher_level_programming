#!/usr/bin/pytho3
"""this is file for task 11"""


class Student:
    """Defines a student."""
    def __init__(self, first_name, last_name, age):
        """Initializes a student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)} 
    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
