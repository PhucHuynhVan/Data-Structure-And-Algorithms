import pytest
from recursion.recursion_interview_problems import (
    recursion_reverse_string_func,
)


@pytest.mark.parametrize("str_input,  out", [
    ('hello', 'olleh'),
    ('hello world', 'dlrow olleh'),
    ('123456789', '987654321'),
])
def test_recursion_reverse_string_func(str_input, out):
    assert recursion_reverse_string_func(str_input) == out
