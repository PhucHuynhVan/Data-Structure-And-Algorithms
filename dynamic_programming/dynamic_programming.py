"""Dynamic programming"""


def fib_memoization(number: int) -> int:
    """Fibonnaci uses memoization"""
    memo = [0, 1]
    for i in range(2, number + 1):
        memo.append(memo[i - 1] + memo[i - 2])
    return memo[number]


def grid_traveler(rows: int, columns: int, memoization: {}) -> int:
    """
    Return the number of paths from the top-left to the bottom-right of the grids (rows x columns)
    """
    matrix_key = str(rows) + "," + str(columns)
    if matrix_key in memoization:
        return memoization[matrix_key]
    if (rows == 0) or (columns == 0):
        return 0
    if (rows == 1) and (columns == 1):
        return 1
    memoization[matrix_key] = grid_traveler(
        rows - 1, columns, memoization
    ) + grid_traveler(rows, columns - 1, memoization)
    return memoization[matrix_key]
