from test_framework import generic_test

import functools


def roman_to_integer(s: str) -> int:
    trans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def _reducer(val, i):
        if trans[s[i + 1]] > trans[s[i]]:
            return val - trans[s[i]]
        else:
            return val + trans[s[i]]

    return functools.reduce(_reducer, reversed(range(len(s) - 1)), trans[s[-1]])


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", "roman_to_integer.tsv", roman_to_integer
        )
    )
