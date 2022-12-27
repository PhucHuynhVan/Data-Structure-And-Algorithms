"""Implement a Queue"""
# pylint: disable=too-few-public-methods


class Queue:
    """Implement a Queue"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Whether the queue is empty"""
        return not self.items

    def enqueue(self, item):
        """Adds a new item to the rear of the queue"""
        return self.items.insert(0, item)

    def dequeue(self):
        """Removes the front item from the queue."""
        return self.items.pop()

    def size(self):
        """Returns the number of items in the queue"""
        return len(self.items)
