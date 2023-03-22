#!/usr/bin/python3
def lookup(obj):
    """
    This function takes an object as an argument and returns a list of all the
    attributes and methods available for that object.
    """
    return [attr for attr in dir(obj)]
