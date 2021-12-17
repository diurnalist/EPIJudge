from test_framework import generic_test
import math

def count_bits(x: int) -> int:
    ret = 0
    while x:
        ret += x & 1
        x >>= 1
    return ret

def count_bits2(x: int) -> int:
    ret = 0
    while x:
        next_set = ~(x-1) & x
        if next_set > 1:
            # Skip over to next set bit
            x >>= int(math.log2(next_set))
        # Increment and pass bit
        x >>= 1
        ret += 1
    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits2))
