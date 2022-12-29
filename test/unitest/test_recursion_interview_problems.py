import pytest
from recursion.recursion_interview_problems import (
    recursion_reverse_string_func,
    recursion_string_permutation_func,
)


@pytest.mark.parametrize("str_input,  out", [
    ('hello', 'olleh'),
    ('hello world', 'dlrow olleh'),
    ('123456789', '987654321'),
])
def test_recursion_reverse_string_func(str_input, out):
    assert recursion_reverse_string_func(str_input) == out


@pytest.mark.parametrize("str_input,  out", [
    ('abc', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']),
    ('dog', ['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']),
])
def test_recursion_string_permutation_func(str_input, out):
    assert sorted(recursion_string_permutation_func(str_input)) == sorted(out)
