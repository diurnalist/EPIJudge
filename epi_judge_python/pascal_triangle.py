from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    tri = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]
    return tri


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "pascal_triangle.py", "pascal_triangle.tsv", generate_pascal_triangle
        )
    )
