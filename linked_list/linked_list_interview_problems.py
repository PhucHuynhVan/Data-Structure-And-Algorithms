"""Linked List Interview Problem"""
# pylint: disable=too-few-public-methods


class Node:
    """A node of an Linked List"""

    def __init__(self, value):
        self.value = value
        self.next_node = None


def singly_linked_list_cycle_check_func(node: Node) -> bool:
    """Singly Linked List Cycle Check - SOLUTION"""
    current_node = node
    next_node = node

    while next_node is not None and next_node.next_node is not None:
        current_node = current_node.next_node
        next_node = next_node.next_node.next_node

        if next_node == current_node:
            return True
    return False


def singly_linked_list_reverse_func(node: Node) -> bool:
    """Linked List Reversal - SOLUTION"""
    current_node = node
    previous_node = None

    while current_node:
        next_node = current_node.next_node
        current_node.next_node = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node


def linked_list_n_from_last_node_func(number_from_last: int, node: Node) -> Node:
    """Linked List Nth to Last Node - SOLUTION"""
    left_point = node
    right_point = node

    for _ in range(number_from_last - 1):

        if not right_point.next_node:
            raise LookupError("Error: n is larger than the length of linked list.")

        right_point = right_point.next_node

    while right_point.next_node:
        left_point = left_point.next_node
        right_point = right_point.next_node

    return left_point
