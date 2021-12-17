from test_framework import generic_test


def divide(x: int, y: int) -> int:
    ret = 0
    power = 32  # why?
    y_power = y << power
    neg = True if x < 0 else False
    x = -x if neg else x
    while x >= y:
        while y_power > x:
            power -= 1
            y_power = y << power
        ret += 1 << power
        x -= y_power
    return -ret if neg else ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
