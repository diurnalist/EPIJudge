from typing import Iterator, List

from test_framework import generic_test

import heapq


def online_median(sequence: Iterator[int]) -> List[float]:
    medians = []
    min_heap, max_heap = [], []
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    for x in sequence:
        # move the smallest of the larger half to the smaller half
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        # move the largest of the smaller half back to the larger half if the smaller
        # half is larger now
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        medians.append(
            (min_heap[0] - max_heap[0]) / 2
            if len(max_heap) == len(min_heap)
            else min_heap[0]
        )

    return medians


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "online_median.py", "online_median.tsv", online_median_wrapper
        )
    )
