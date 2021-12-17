from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    x_str = str(x)
    x_len = len(x_str)
    for i in range(x_len):
        if x_str[i] != x_str[(x_len-1)-i]:
            return False
    return True


import math


def is_palindrome_number2(x: int) -> bool:
    if x <= 0:
        return x == 0

    x_digs = math.floor(math.log10(x)) + 1
    h_mult = 10 ** (x_digs - 1)
    for _ in range(x_digs // 2):
        if x % 10 != x // h_mult:
            return False
        x %= h_mult
        x //= 10
        h_mult //= 100
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number2))
