from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import namedtuple

class Stack:
    StackItem = namedtuple("Stackitem", ["data", "prior_max"])

    def __init__(self):
        self._items = []
        self._max = None

    def empty(self) -> bool:
        return not self._items

    def max(self) -> int:
        return self._max

    def pop(self) -> int:
        item = self._items.pop()
        self._max = item.prior_max
        return item.data

    def push(self, x: int) -> None:
        self._items.append(self.StackItem(x, self._max))
        self._max = max(self._max, x) if self._max else x


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
