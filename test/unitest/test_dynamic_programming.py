import pytest
from dynamic_programming.dynamic_programming import (
    fib_memoization,
    grid_traveler,
)


@pytest.mark.parametrize("n, out", [
    (2, 1),
    (5, 5)
])
def test_fib_memoization_func(n, out):
    assert fib_memoization(n) == out


@pytest.mark.parametrize("m, n, out", [
    (2, 3, 3),
    (18, 18, 2333606220)
])
def test_grid_traveler_func(m, n, out):
    assert grid_traveler(m, n, {}) == out
