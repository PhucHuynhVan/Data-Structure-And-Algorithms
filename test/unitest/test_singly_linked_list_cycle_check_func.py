import pytest
from linked_list.linked_list_interview_problems import (
    Node,
    singly_linked_list_cycle_check_func,
)


def test_singly_linked_list_cycle_check_func():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next_node = b
    b.next_node = c
    c.next_node = a
    assert singly_linked_list_cycle_check_func(a) == True
    c.next_node = None
    assert singly_linked_list_cycle_check_func(a) == False
