from test_framework import generic_test


def parity(x: int) -> int:
    """Parity is 1 for input with an odd number of set bits, 0 otherwise."""
    ret = 0
    while x:
        # Remove last set bit in x
        x &= (x-1)
        # Swap b/w even and odd
        ret ^= 1
    return ret

def parity2(x: int) -> int:
    """faster implementation that takes associativity and communativity of parity into account."""
    bitchunk = 32
    while bitchunk:
        x ^= x >> bitchunk
        bitchunk >>= 1
    return x & 0x1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity2))
