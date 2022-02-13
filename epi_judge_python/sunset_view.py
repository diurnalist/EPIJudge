from typing import Iterator, List

from test_framework import generic_test
from collections import namedtuple


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    Building = namedtuple("Building", ["idx", "height"])
    with_view = []
    for i, height in enumerate(sequence):
        while with_view and with_view[-1].height <= height:
            with_view.pop()
        with_view.append(Building(i, height))
    return [bldg.idx for bldg in reversed(with_view)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sunset_view.py", "sunset_view.tsv", examine_buildings_with_sunset
        )
    )
