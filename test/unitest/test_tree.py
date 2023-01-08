import pytest
from tree.tree import (
    binary_tree_depth_first_value_traversal,
    binary_tree_breadth_first_value_traversal,
    is_binary_tree_includes,
    sum_binary_tree_iterative,
    sum_binary_tree_recursion,
    BinaryTree,
)


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


@pytest.mark.parametrize("target, out", [
    ('e',  True),
    ('j', False),
])
def test_binary_tree_breadth_first_value_traversal_fun(target, out):
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
    result = is_binary_tree_includes(a, target)
    # Assert
    assert result == out


def test_sum_binary_tree():
    # Arr
    a = BinaryTree(1)
    b = BinaryTree(2)
    c = BinaryTree(3)
    d = BinaryTree(4)
    e = BinaryTree(5)
    f = BinaryTree(6)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    # Act
    result_iterative = sum_binary_tree_iterative(a)
    result_recursion = sum_binary_tree_recursion(a)
    # Assert
    assert result_iterative == result_recursion == 21
