import pytest
from array_sequences.largest_continuous_sum.largest_continuous_sum import largest_continuous_sum


@pytest.mark.parametrize("arr,  out", [
    ([1, 2, -1, 3, 4, -1], 9),
    ([1, 2, -1, 3, 4, 10, 10, -10, -1], 29),
    ([-1, 1], 1),
])
def test_largest_continuous_sum_func(arr, out):
    assert largest_continuous_sum(arr) == out
