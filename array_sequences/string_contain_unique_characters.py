"""Unique Characters in String"""


def string_contain_unique_characters_func(string: str) -> bool:
    """Unique Characters in String Func"""
    chars = set()
    for char in string:
        if char in chars:
            return False
        chars.add(char)
    return True
