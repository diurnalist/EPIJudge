from test_framework import generic_test

import string


def is_palindrome(s: str) -> bool:
    return all(
        x == y
        for x, y in zip(
            map(str.lower, filter(str.isalnum, s)),
            map(str.lower, filter(str.isalnum, reversed(s))),
        )
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_palindromic_punctuation.py",
            "is_string_palindromic_punctuation.tsv",
            is_palindrome,
        )
    )
