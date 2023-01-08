from tree.tree import (
    binary_tree_depth_first_value_traversal,
    binary_tree_breadth_first_value_traversal,
    BinaryTree,
)
from stacks_queues_deques.stack import Stack
from stacks_queues_deques.queue import Queue


def test_binary_tree_depth_first_value_traversal_fun():
    # Arr
    a = BinaryTree('a')
    b = BinaryTree('b')
    c = BinaryTree('c')
    d = BinaryTree('d')
    e = BinaryTree('e')
    f = BinaryTree('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    # Act
    result = binary_tree_depth_first_value_traversal(a)
    # Assert
    assert result is not None
    assert result == ['a', 'b', 'd', 'e', 'c', 'f']


def test_binary_tree_breadth_first_value_traversal_fun():
    # Arr
    a = BinaryTree('a')
    b = BinaryTree('b')
    c = BinaryTree('c')
    d = BinaryTree('d')
    e = BinaryTree('e')
    f = BinaryTree('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    # Act
    result = binary_tree_breadth_first_value_traversal(a)
    # Assert
    assert result is not None
    assert result == ['a', 'b', 'c', 'd', 'e', 'f']
