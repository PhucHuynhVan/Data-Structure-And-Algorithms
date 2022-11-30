import pytest
from Lesson_1_Binary_Search_Linked_Lists_and_Complexity.lession_1 import locate_card_liner_search


@pytest.mark.parametrize("cards, query, out",[
    ([13, 11, 10, 7, 4, 3, 1, 0], 7, 3),
    ([13, 11, 10, 7, 4, 3, 1, 0], 1, 6),
    ([4, 2, 1, -1], 4, 0),
])
def test_liner_search_locate_card(cards, query, out):
    # Act
    func_out = locate_card_liner_search(cards, query)
    assert func_out == out


