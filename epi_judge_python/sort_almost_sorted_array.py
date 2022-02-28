from typing import Iterator, List

from test_framework import generic_test

import heapq
import itertools


def sort_approximately_sorted_array(sequence: Iterator[int], k: int) -> List[int]:
    k_heap = []
    heapq.heapify(k_heap)
    for x in itertools.islice(sequence, k + 1):
        heapq.heappush(k_heap, x)

    sorted_seq = []
    for x in sequence:
        sorted_seq.append(heapq.heappushpop(k_heap, x))

    while k_heap:
        sorted_seq.append(heapq.heappop(k_heap))

    return sorted_seq


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py",
            "sort_almost_sorted_array.tsv",
            sort_approximately_sorted_array_wrapper,
        )
    )
