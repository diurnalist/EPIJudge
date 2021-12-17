import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    """Find intersection of two rects and return intersecting rect, if any."""
    leftmost, rightmost = (r1, r2) if r1.x < r2.x else (r2, r1)
    bottommost, topmost = (r1, r2) if r1.y <  r2.y else (r2, r1)
    inter = Rect(
        rightmost.x,
        topmost.y,
        min((leftmost.x + leftmost.width) - rightmost.x, rightmost.width),
        min((bottommost.y + bottommost.height) - topmost.y, topmost.height)
    )
    return inter if inter.width >= 0 and inter.height >= 0 else Rect(0, 0, -1, -1)



def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
