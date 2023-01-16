import pytest
from dynamic_programming.dynamic_programming import fib_memoization


@pytest.mark.parametrize("n, out", [
    (2, 1),
    (5, 5)
])
def test_fib_memoization_func(n, out):
    assert fib_memoization(n) == out
