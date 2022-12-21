"""Find missing element solution"""
from typing import List
from collections import defaultdict


def finder(arr_1: List[int], arr_2: List[int]) -> int:
    """sum_pair func"""
    df_dict = defaultdict(int)
    for num in arr_2:
        df_dict[num] += 1

    for num in arr_1:
        if df_dict[num] == 0:
            return num
        df_dict[num] -= 1
    return -1
