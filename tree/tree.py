"""Nodes and References Implementation of a Tree"""
from typing import Type
from stacks_queues_deques.stack import Stack
# pylint: disable=too-few-public-methods


class BinaryTree:
    """Nodes and References Implementation of a Tree"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        """Insert left to Tre"""
        new_left = BinaryTree(new_node)
        if self.left is None:
            self.left = new_left
        else:
            new_left.left = self.left
            self.left = new_left

    def insert_right(self, new_node):
        """Insert right to Tree"""
        new_right = BinaryTree(new_node)
        if self.right is None:
            self.right = new_right
        else:
            new_right.right = self.right
            self.right = new_right

    def get_child_left(self):
        """Get left child"""
        return self.left

    def get_child_right(self):
        """Get right child"""
        return self.right

    def set_root_val(self, new_val):
        """Set node value"""
        self.val = new_val

    def get_root_val(self):
        """Get node value"""
        return self.val


def binary_tree_traversal(tree: BinaryTree) -> Type[Stack]:
    """Traversal the Binary Tree"""
    result = Stack()
    stacks = Stack()
    stacks.push(tree)
    while stacks.size() > 0:
        current = stacks.pop()
        result.push(current.val)
        if current.right:
            stacks.push(current.right)
        if current.left:
            stacks.push(current.left)
    return result
