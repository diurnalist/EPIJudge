from typing import List

from test_framework import generic_test


import heapq
import itertools


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    class Monotonic:
        def __init__(self):
            self._last = float("-inf")

        def __call__(self, curr):
            result = curr < self._last
            self._last = curr
            return result

    # leverage property of groupby where it will group subsequent entries
    # if they pass equality checks. Monotonic() will return True if the series
    # is increasing, False otherwise, so it will demarcate the peaks and valleys
    # as the monotonicity changes.
    subarrays = itertools.groupby(A, Monotonic())
    return list(
        heapq.merge(
            *[
                list(group)[:: -1 if is_decreasing else 1]
                for is_decreasing, group in subarrays
            ]
        )
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_increasing_decreasing_array.py",
            "sort_increasing_decreasing_array.tsv",
            sort_k_increasing_decreasing_array,
        )
    )
