import pytest
from array_sequences.sentence_reversal import sentence_reversal_func


@pytest.mark.parametrize("str_input,  out", [
    ('    space before', 'before space'),
    ('space after     ', 'after space'),
    ('   Hello John    how are you   ', 'you are how John Hello'),
    ('1', '1'),
])
def test_sentence_reversal_func(str_input, out):
    assert sentence_reversal_func(str_input) == out
