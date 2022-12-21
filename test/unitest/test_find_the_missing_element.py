import pytest
from array_sequences.find_the_missing_element.find_the_missing_element import finder


@pytest.mark.parametrize("arr1, arr2, out", [
    ([5, 5, 7, 7], [5, 7, 7], 5),
    ([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6], 5),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1], 6),
])
def test_finder_func(arr1, arr2, out):
    assert finder(arr1, arr2) == out
