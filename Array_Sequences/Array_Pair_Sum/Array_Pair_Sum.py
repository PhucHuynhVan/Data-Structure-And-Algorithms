from typing import List


def sum_pair(arr: List[int], k: int):
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
    return "\n".join(map(str, list(output)))


if __name__ == "__main__":
    print(sum_pair([1, 3, 2, 2], 4))
    print(sum_pair([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10))
