"""Using dynamic programming"""


def fib_memoization(number: int) -> int:
    """Fibonnaci uses memoization"""
    memo = [0, 1]
    for i in range(2, number + 1):
        memo.append(memo[i-1] + memo[i-2])
    return memo[number]
