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


def fibonnaci_sequence_dynamically_func(number: int) -> int:
    """Fibonnaci Sequence Implementation"""
    fib_cache = [0, 1]

    for i in range(2, number + 1):
        fib_cache.append(fib_cache[i - 1] + fib_cache[i - 2])
    return fib_cache[number]


def change_coin_dynamically_func(target: int, coins: List[int]):
    """
    INPUT: Target change amount and list of coin values
    OUTPUT: Minimum coins needed to make change

    Note, this solution is not optimized.
    """
    combinations = [target + 1] * (target + 1)
    combinations[0] = 0
    for i in range(1, len(combinations)):
        for coin in coins:
            if i - coin >= 0:
                combinations[i] = min(combinations[i], 1+combinations[i - coin])
    return combinations[target] if combinations[target] != target + 1 else -1
