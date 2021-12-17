from test_framework import generic_test


def power(x: float, y: int) -> float:
    """Compute x^y.

    Brute force is x*x*x*x...

    If k is even, x^k = x^(k/2)^2
    If k is odd, x^k = x* x^(k/2)^2

    And x^k1 * x^k2 = x^(k1 + k2)
    """
    ret, pow = 1.0, y
    if y < 0:
        pow, x = -pow, 1/x
    while pow:
        if pow & 1:
            ret *= x
        x, pow = x * x, pow >> 1
    return ret


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
