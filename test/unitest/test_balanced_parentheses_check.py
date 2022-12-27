import pytest
from stacks_queues_deques.balanced_parentheses_check import balanced_parentheses_check_func


@pytest.mark.parametrize("parens_str,  out", [
    ('[]', True),
    ('[](){([[[]]])}', True),
    ('()(){]}', False),
])
def test_balanced_parentheses_check_func(parens_str, out):
    assert balanced_parentheses_check_func(parens_str) == out
