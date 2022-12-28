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
