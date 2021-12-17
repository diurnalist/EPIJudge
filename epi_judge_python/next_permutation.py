from typing import List

from test_framework import generic_test


# 1,2,3 => 1,3,2
# 1,3,2 => 2,1,3
# 2,1,3 => 2,3,1
# 2,3,1 => 3,1,2
import math


def next_permutation(perm: List[int]) -> List[int]:
    inv_pt = len(perm) - 2
    while inv_pt >= 0 and perm[inv_pt + 1] <= perm[inv_pt]:
        inv_pt -= 1
    if inv_pt == -1:
        return []
    for i in reversed(range(inv_pt + 1, len(perm))):
        if perm[i] > perm[inv_pt]:
            perm[i], perm[inv_pt] = perm[inv_pt], perm[i]
            break
    return perm[: inv_pt + 1] + list(reversed(perm[inv_pt + 1 :]))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", "next_permutation.tsv", next_permutation
        )
    )
