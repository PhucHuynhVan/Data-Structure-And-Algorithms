"""Recursion Interview Problems"""
from typing import List


def recursion_reverse_string_func(string: str) -> str:
    """Reverse a String Func"""
    if len(string) <= 1:
        return string

    return recursion_reverse_string_func(string[1:]) + string[0]


def recursion_string_permutation_func(string: str) -> List[str]:
    """String Permutation Func"""
    out = []
    if len(string) == 1:
        out = [string]
    else:
        for i, let in enumerate(string):
            out += [let + perm for perm in recursion_string_permutation_func(
                string[:i] + string[i + 1:])]
    return out


def recursion_fibonnaci_sequence_func(number: int) -> int:
    """Fibonnaci Sequence Implementation"""
    if number in (0, 1):
        return number

    return recursion_fibonnaci_sequence_func(number-1) + recursion_fibonnaci_sequence_func(number-2)
