from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return "0"

    sign = ""
    if x < 0:
        x, sign = -x, "-"

    s_lst = []
    while x > 0:
        s_lst.append(chr(ord("0") + x % 10))
        x //= 10
    return sign + "".join(reversed(s_lst))


import string


def string_to_int(s: str) -> int:
    ret = 0
    digits = len(s)
    if s.startswith("-") or s.startswith("+"):
        digits -= 1
    factor = 1
    for i in range(digits):
        ret += string.digits.index(s[~i]) * factor
        factor *= 10
    return -ret if s.startswith("-") else ret


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_integer_interconversion.py",
            "string_integer_interconversion.tsv",
            wrapper,
        )
    )
