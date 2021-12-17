from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    furthest = 0
    for i, steps in enumerate(A):
        if i > furthest:
            return False
        furthest = max(furthest, i + steps)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
