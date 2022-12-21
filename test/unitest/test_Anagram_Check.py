import pytest
from Array_Sequences.Anagram_Check.Anagram_Check import anagram_check


@pytest.mark.parametrize("str_1, str_2, out", [
    ('go go go', 'gggooo', True),
    ('abc', 'cba', True),
    ('hi man', 'hi     man', True),
    ('aabbcc', 'aabbc', False),
    ('123', '1 2', False)
])
def test_anagram_func(str_1, str_2, out):
    assert anagram_check(str_1, str_2) == out
