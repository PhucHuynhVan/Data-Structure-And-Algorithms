import pytest
from array_sequences.array_pair_sum.array_pair_sum import sum_pair


@pytest.mark.parametrize("arr, k, out", [
    ([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10, 6),
    ([1, 2, 3, 1], 3, 1),
    ([1, 3, 2, 2], 4, 2),
])
def test_sum_pair_func(arr, k, out):
    assert sum_pair(arr, k) == out
