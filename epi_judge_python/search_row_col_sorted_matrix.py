from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    row, col = 0, len(A[0]) - 1
    while row < len(A) and col > -1:
        if x == A[row][col]:
            return True
        if x > A[row][col]:
            row += 1
        else:
            col -= 1
    return False


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_row_col_sorted_matrix.py",
            "search_row_col_sorted_matrix.tsv",
            matrix_search,
        )
    )
