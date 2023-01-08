"""Implement Deque"""
# pylint: disable=too-few-public-methods


class Deque:
    """Implement Deque"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Whether the queue is empty"""
        return not self.items

    def add_front(self, item):
        """Add from Front"""
        self.items.append(item)

    def add_rear(self, item):
        """Add from Rear"""
        self.items.insert(0, item)

    def remove_front(self):
        """Removes from Font"""
        return self.items.pop()

    def remove_rear(self):
        """Remove from Rear"""
        return self.items.pop(0)

    def size(self):
        """Returns the number of items in the deque"""
        return len(self.items)
