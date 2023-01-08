"""Recursion Homework Problems"""


def recursion_calculate_sum_n_integer(numbers: int) -> int:
    """Takes an integer and computes the cumulative sum of 0 to that integer"""
    if numbers == 0:
        return 0

    return numbers + recursion_calculate_sum_n_integer(numbers - 1)


def recursion_sum_of_all_the_individual_digits(numbers: int) -> int:
    """returns the sum of all the individual digits in that integer."""
    if numbers < 10:
        return numbers

    return numbers % 10 + recursion_sum_of_all_the_individual_digits(int(numbers / 10))
