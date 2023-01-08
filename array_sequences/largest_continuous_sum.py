"""Largest continuous sum"""
from typing import List


def largest_continuous_sum(arr: List[int]) -> int:
    "largest_continuous_sum func"
    if len(arr) == 0:
        return 0

    current_sum = max_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)

        max_sum = max(current_sum, max_sum)
    return max_sum
