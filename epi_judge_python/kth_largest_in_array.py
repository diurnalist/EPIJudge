from typing import List

from test_framework import generic_test


import random

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    # find all values less than pivot
    # and those greater than pivot
    # if len(greater) > k, search again inside it
    # if len(greater) < k, subtract from k and search again inside lesser
    def rand_pivot(start, end):
        pivot_i = random.randint(start, end)
        pivot_value = A[pivot_i]
        # Put the pivot at the end of the list
        A[end], A[pivot_i] = A[pivot_i], A[end]
        new_pivot_i = start
        for i in range(start, end):
            if A[i] > pivot_value:
                A[i], A[new_pivot_i] = A[new_pivot_i], A[i]
                new_pivot_i += 1
        A[end], A[new_pivot_i] = A[new_pivot_i], A[end]
        return new_pivot_i

    start, end = 0, len(A) - 1
    while start <= end:
        pivot_i = rand_pivot(start, end)
        if pivot_i == k - 1:
            return A[pivot_i]
        elif pivot_i > k - 1:
            end = pivot_i - 1
        else:
            start = pivot_i + 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "kth_largest_in_array.py", "kth_largest_in_array.tsv", find_kth_largest
        )
    )
