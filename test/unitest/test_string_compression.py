import pytest
from array_sequences.string_compression import string_compression_func


@pytest.mark.parametrize("str_input,  out", [
    ('', ''),
    ('AABBCC', 'A2B2C2'),
    ('AAABCCDDDDD', 'A3B1C2D5'),
])
def test_string_compression_func(str_input, out):
    assert string_compression_func(str_input) == out
