"""
A very common interview question is to begin by just implementing a Stack! Try your best to
implement your own stack!

It should have the methods:

Check if its empty
Push a new item
Pop an item
Peek at the top item
Return the size
"""
# pylint: disable=too-few-public-methods


class Stack:
    """Implement a Stack"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check stack is empty"""
        return not self.items

    def push(self, item):
        """Push a new item"""
        self.items.append(item)

    def pop(self):
        """Pop an item"""
        return self.items.pop()

    def peek(self):
        """Peek at the top item"""
        return self.items[len(self.items) - 1]

    def size(self):
        """Return the size"""
        return len(self.items)
