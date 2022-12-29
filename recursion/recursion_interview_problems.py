"""Recursion Interview Problems"""


def recursion_reverse_string_func(string: str) -> str:
    """Reverse a String"""
    if len(string) <= 1:
        return string

    return recursion_reverse_string_func(string[1:]) + string[0]
