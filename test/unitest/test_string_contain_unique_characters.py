import pytest
from array_sequences.string_contain_unique_characters import string_contain_unique_characters_func


@pytest.mark.parametrize("str_input,  out", [
    ('', True),
    ('goo', False),
    ('abcdefg', True),
])
def test_string_contain_unique_characters(str_input, out):
    assert string_contain_unique_characters_func(str_input) == out
