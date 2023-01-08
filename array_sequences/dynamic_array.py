"""Dynamic Array Implementation"""
import ctypes


class DynamicArray:
    """DYNAMIC ARRAY CLASS (Similar to Python List)"""

    def __init__(self):
        self.actual_element = 0
        self.capacity = 1
        self.arr = self.make_array(self.capacity)

    def __len__(self):
        """Return number of elements sorted in array"""
        return self.actual_element

    def __getitem__(self, index):
        """Return element at index index"""
        if not 0 <= index < self.actual_element:
            return IndexError("Out of bound")
        return self.arr[index]

    def append(self, ele):
        """Add new element of the array"""
        if self.actual_element == self.capacity:
            self._resize(2 * self.capacity)

        self.arr[self.actual_element] = ele
        self.actual_element += 1

    def _resize(self, new_cap):
        """Resize internal array to capacity new_cap"""
        new_arr = self.make_array(new_cap)
        for k in range(self.actual_element):
            new_arr[k] = self.arr[k]

        self.arr = new_arr
        self.capacity = new_cap

    def make_array(self, new_cap):
        """Returns a new array with new_cap capacity"""
        return (new_cap * ctypes.py_object)()
