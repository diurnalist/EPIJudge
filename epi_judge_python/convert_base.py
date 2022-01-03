from test_framework import generic_test

import functools
import string


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    def from_base10(b10_num, b):
        return (
            ""
            if b10_num == 0
            else from_base10(b10_num // b, b) + string.hexdigits[b10_num % b].upper()
        )

    b10_num = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[num_as_string[0] in "-+" :],
        0,
    )
    ret = ("-" if num_as_string.startswith("-") else "") + (
        "0" if b10_num == 0 else from_base10(b10_num, b2)
    )
    return ret


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "convert_base.py", "convert_base.tsv", convert_base
        )
    )
