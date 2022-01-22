from test_framework import generic_test

import functools


def rabin_karp(t: str, s: str) -> int:
    if len(t) < len(s):
        return -1

    base = 26  # alphabet
    # start the rolling hash of t
    t_hash = functools.reduce(lambda h, c: h * base + ord(c), t[: len(s)], 0)
    # generate the search fingerprint for s
    s_hash = functools.reduce(lambda h, c: h * base + ord(c), s, 0)
    power_s = base ** max(len(s) - 1, 0)  # in order to pop off the first char

    for i in range(len(s), len(t)):
        # double-check value to avoid hash collision
        if t_hash == s_hash and t[i - len(s) : i] == s:
            return i - len(s)

        t_hash -= ord(t[i - len(s)]) * power_s
        t_hash = t_hash * base + ord(t[i])

    # edge case: if we matched at the very end
    if t_hash == s_hash and t[-len(s) :] == s:
        return len(t) - len(s)

    return -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "substring_match.py", "substring_match.tsv", rabin_karp
        )
    )
