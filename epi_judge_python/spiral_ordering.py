from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    size = len(square_matrix)
    if size < 1:
        return []

    # take the first row
    ordered = square_matrix[0]
    # handle 1xN case
    if size == 1:
        return ordered

    remaining = square_matrix[1:]
    # then the last column
    for row in remaining:
        ordered.append(row.pop())

    # then the bottom row (reversed)
    ordered += reversed(remaining.pop())

    # then the first column (reversed)
    for row in reversed(remaining):
        ordered.append(row.pop(0))

    # then add the result of the inner box
    return ordered + matrix_in_spiral_order(remaining)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "spiral_ordering.py", "spiral_ordering.tsv", matrix_in_spiral_order
        )
    )
