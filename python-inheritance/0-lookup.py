#!/usr/bin/python3

def lookup(obj):
    """
    This function returns a list of all the attributes and methods available
    for an object.

    Args:
    - obj: An object of any type

    Returns:
    - A list of strings representing the available attributes and methods
      of the given object.
    """
    return [attr for attr in dir(obj)]
