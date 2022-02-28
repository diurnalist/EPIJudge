from typing import List

from test_framework import generic_test

import heapq


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    heap = [(l[0], i, 0) for i, l in enumerate(sorted_arrays)]
    heapq.heapify(heap)
    merged = []
    while heap:
        x, outer_idx, inner_idx = heapq.heappop(heap)
        merged.append(x)
        inner_idx += 1
        if inner_idx < len(sorted_arrays[outer_idx]):
            heapq.heappush(
                heap, (sorted_arrays[outer_idx][inner_idx], outer_idx, inner_idx)
            )
    return merged


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_arrays_merge.py", "sorted_arrays_merge.tsv", merge_sorted_arrays
        )
    )
