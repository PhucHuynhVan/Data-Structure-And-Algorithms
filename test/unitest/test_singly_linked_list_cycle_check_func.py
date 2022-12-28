import pytest
from linked_list.linked_list_interview_problems import (
    Node,
    singly_linked_list_cycle_check_func,
    singly_linked_list_reverse_func,
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


def test_singly_linked_list_reverse_func():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.next_node = b
    b.next_node = c
    c.next_node = d
    assert a.next_node.value == b.value
    assert b.next_node.value == c.value
    assert c.next_node.value == d.value
    singly_linked_list_reverse_func(a)
    assert d.next_node.value == c.value
    assert c.next_node.value == b.value
    assert b.next_node.value == a.value
