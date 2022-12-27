"""Balanced Parentheses Check"""


def balanced_parentheses_check_func(parens_str: str) -> bool:
    """Balanced Parentheses Check Function"""
    if len(parens_str) % 2 != 0:
        return False

    stack = []
    opening_parens = set('([{')
    pair_parens = {('(', ')'), ('[', ']'), ('{', '}')}

    for paren in parens_str:
        if paren in opening_parens:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False

            last_opening_paren = stack.pop()
            if (last_opening_paren, paren) not in pair_parens:
                return False
    return len(stack) == 0
