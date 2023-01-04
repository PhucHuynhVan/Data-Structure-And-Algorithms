"""Recursion Homework Problems"""


def recursion_calculate_sum_n_integer(numbers: int) -> int:
    """Takes an integer and computes the cumulative sum of 0 to that integer"""
    if numbers == 0:
        return 0

    return numbers + recursion_calculate_sum_n_integer(numbers-1)
