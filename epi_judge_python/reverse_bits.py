from test_framework import generic_test


PRECMP = [
    0b0000,  # 0000
    0b1000,  # 0001
    0b0100,  # 0010
    0b1100,  # 0011
    0b0010,  # 0100
    0b1010,  # 0101
    0b0110,  # 0110
    0b1110,  # 0111
    0b0001,  # 1000
    0b1001,  # 1001
    0b0101,  # 1010
    0b1101,  # 1011
    0b0011,  # 1100
    0b1011,  # 1101
    0b0111,  # 1110
    0b1111,  # 1111
]

def reverse_bits(x: int) -> int:
    bitlen = 64
    masksize = 4
    bitmask = 0xF
    rev = PRECMP[x & bitmask]
    for i in range(1, int(bitlen/masksize)):
        rev <<= masksize
        rev |= PRECMP[(x >> (masksize*i)) & bitmask]
    return rev


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
