"""Sum pair solution"""
from typing import List


def sum_pair(arr: List[int], k: int):
    """sum_pair func"""
    # The edge case
    if len(arr) < 2:
        return ""

    seen = set()
    output = set()

    # iterate num in arr
    for num in arr:

        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
    # return "\n".join(map(str, list(output)))
    return len(output)
