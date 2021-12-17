from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    """
    Flipping two bits will increase the result by 2^i
    but decrease it by 2^j where i and j are bit positions
    and i > j. Bits must not be equal.

    Try to find min of 2^i - 2^j.

    Consider that if we are flipping bits, there will always
    be a "leverage" point where the bits differ. it would never
    make sense to flip two bits further from this leverage point,
    e.g., flipping 110 => 011 is always worse than 110 => 101.

    Consider also that we should find this leverage point at the
    smallest possible i. Therefore the two rightmost bits that
    differ should be flipped.
    """
    bitlen = 64
    for i in range(bitlen):
        j = i + 1
        if ((x >> i) & 0x1 != (x >> j) & 0x1):
            x ^= (1 << i) | (1 << j)
            return x
    raise ValueError("no bits differ")


def closest_int_same_bit_count2(x: int) -> int:
    """Same as above but O(1) time + space"""
    # Find last differing bits
    last_set = x & ~(x - 1)
    last_unset = ~x & ~(~x - 1)
    if not x or not last_set:
        raise ValueError("no bits differ")
    # Need to find which mask starts past the LSB
    mask = last_set if last_set > 1 else last_unset
    mask |= mask >> 1
    return x ^ mask


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count2))
