#!/usr/bin/python3
"""
MyList module
"""


class MyList(list):
    """
    MyList class that inherits from list
    """

    def print_sorted(self):
        """
        Public instance method that prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
