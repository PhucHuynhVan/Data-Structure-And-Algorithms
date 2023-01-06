from tree.tree import (
    binary_tree_traversal,
    BinaryTree,
)
from stacks_queues_deques.stack import Stack


def test_binary_tree_traversal():
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
    result = binary_tree_traversal(a)
    # Assert
    assert isinstance(result, Stack)
    assert not result.is_empty()
    assert result.items == ['a', 'b', 'd', 'e', 'c', 'f']
