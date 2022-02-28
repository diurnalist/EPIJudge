from typing import List

from test_framework import generic_test, test_utils

import heapq


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if k <= 0:
        return []
    candidates = [(-A[0], 0)]
    heapq.heapify(candidates)
    largest = []
    for _ in range(k):
        idx = candidates[0][1]
        largest.append(-heapq.heappop(candidates)[0])
        l_idx, r_idx = 2 * idx + 1, 2 * idx + 2
        # take a look at the children of what we just popped (b/c it was the biggest)
        if l_idx < len(A):
            heapq.heappush(candidates, (-A[l_idx], l_idx))
        if r_idx < len(A):
            heapq.heappush(candidates, (-A[r_idx], r_idx))
    return largest


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare,
        )
    )
