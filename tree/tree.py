"""Nodes and References Implementation of a Tree"""
from stacks_queues_deques.stack import Stack
from stacks_queues_deques.queue import Queue
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


def binary_tree_depth_first_value_traversal(tree: BinaryTree) -> list:
    """Traversal the Binary Tree Depth First"""
    if not tree:
        return []
    result = []
    stacks = Stack()
    stacks.push(tree)
    while stacks.size() > 0:
        current = stacks.pop()
        result.append(current.val)
        if current.right:
            stacks.push(current.right)
        if current.left:
            stacks.push(current.left)
    return result


def binary_tree_breadth_first_value_traversal(tree: BinaryTree) -> list:
    """Traversal the Binary Tree Depth First"""
    if not tree:
        return []
    result = []
    queues = Queue()
    queues.enqueue(tree)
    while queues.size() > 0:
        current = queues.dequeue()
        result.append(current.val)
        if current.left:
            queues.enqueue(current.left)
        if current.right:
            queues.enqueue(current.right)
    return result
