import pytest
from recursion.recursion_homework_problems import (
    recursion_calculate_sum_n_integer,
    recursion_sum_of_all_the_individual_digits,
)


@pytest.mark.parametrize("number, out", [
    (4, 10),
    (0, 0),
])
def test_recursion_calculate_sum_n_integer(number, out):
    assert recursion_calculate_sum_n_integer(number) == out


@pytest.mark.parametrize("number, out", [
    (4231, 10),
    (9, 9),
])
def test_recursion_sum_of_all_the_individual_digits(number, out):
    assert recursion_sum_of_all_the_individual_digits(number) == out
