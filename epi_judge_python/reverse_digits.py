from test_framework import generic_test


def reverse(x: int) -> int:
    ret, x1 = 0, abs(x)
    while x1:
        ret = (ret * 10) + (x1 % 10)
        x1 //= 10
    return -ret if x < 0 else ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
