#!/usr/bin/python3
"""
this is my response to the advanced task 12
about inherites int
"""


class MyInt(int):
    """
    this is the module for this answer
    """
    def __eq__(self, other):
        """this is for the equal."""
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
