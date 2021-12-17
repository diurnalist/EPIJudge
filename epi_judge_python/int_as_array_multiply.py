from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    if num1[0] == 0 or num2[0] == 0:
        return [0]
    prod = [0]*(len(num1) + len(num2))
    for pow, d1 in enumerate(reversed(num1)):
        i = len(num1) + len(num2) - pow
        for d2 in reversed(num2):
            i -= 1
            prod[i] += abs(d1 * d2)
            prod[i - 1] += prod[i] // 10
            prod[i] %= 10
    if prod[0] == 0:
        prod = prod[1:]
    if (num1[0] < 0) ^ (num2[0] < 0):
        prod[0] = -prod[0]
    return prod


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
