import pytest
from recursion.recursion_homework_problems import (
    recursion_calculate_sum_n_integer,
)


@pytest.mark.parametrize("number, out", [
    (4, 10),
    (0, 0),
])
def test_recursion_calculate_sum_n_integer(number, out):
    assert recursion_calculate_sum_n_integer(number) == out