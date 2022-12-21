import pytest
from array_sequences.anagram_check.anagram_check import anagram_check


@pytest.mark.parametrize("str_1, str_2, out", [
    ('go go go', 'gggooo', True),
    ('abc', 'cba', True),
    ('hi man', 'hi     man', True),
    ('aabbcc', 'aabbc', False),
    ('123', '1 2', False)
])
def test_anagram_func(str_1, str_2, out):
    assert anagram_check(str_1, str_2) == out
