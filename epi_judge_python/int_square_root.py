from test_framework import generic_test

import math


def square_root(k: int) -> int:
    left, right = 0, k
    while left <= right:
        mid = left + (right - left) // 2
        square = mid**2
        if square == k:
            return mid
        elif square > k:
            right = mid - 1
        else:
            left = mid + 1
    return left - 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_square_root.py", "int_square_root.tsv", square_root
        )
    )
