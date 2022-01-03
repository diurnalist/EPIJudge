import collections
from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
import itertools
import math


def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    qd_size = int(math.sqrt(len(partial_assignment)))
    counts = collections.Counter(
        k
        for i, row in enumerate(partial_assignment)
        for j, c in enumerate(row)
        if c != 0
        for k in ((i, str(c)), (str(c), j), (i // qd_size, j // qd_size, str(c)))
    )
    return max(counts.values(), default=0) <= 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_valid_sudoku.py", "is_valid_sudoku.tsv", is_valid_sudoku
        )
    )
