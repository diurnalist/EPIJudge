from test_framework import generic_test


def swap_bits(x, i, j):
    # Check if bits are different
    if ((x >> i & 0x1) == (x >> j & 0x1)):
        return x
    # Flip each using xor mask
    mask = (1 << i) | (1 << j)
    return x ^ mask


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
