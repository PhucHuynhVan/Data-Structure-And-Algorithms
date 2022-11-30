import pytest
from Lesson_1_Binary_Search_Linked_Lists_and_Complexity.lession_1 import locate_card_liner_search


@pytest.mark.parametrize("cards, query, out",[
    ([13, 11, 10, 7, 4, 3, 1, 0], 7, 3),
    ([13, 11, 10, 7, 4, 3, 1, 0], 1, 6),
    ([4, 2, 1, -1], 4, 0),
    ([3, -1, -9, -127], -127, 3),
    ([6], 6, 0),
    ([9, 7, 5, 2, -9], 4, -1),
    ([], 7, -1),
    ([8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 3, 7)
])
def test_liner_search_locate_card(cards, query, out):
    # Act
    func_out = locate_card_liner_search(cards, query)
    assert func_out == out


