from typing import List
from collections import defaultdict


def finder(arr_1: List[int], arr_2: List[int]) -> int:
    d = defaultdict(int)
    for num in arr_2:
        d[num] += 1

    for num in arr_1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


if __name__ == "__main__":
    print(finder([5, 5, 7, 7], [5, 7, 7]))
    print(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
    print(finder([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]))
