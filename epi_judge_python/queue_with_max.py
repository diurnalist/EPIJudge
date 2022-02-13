from test_framework import generic_test
from test_framework.test_failure import TestFailure

import collections


class QueueWithMax:
    data = collections.deque()
    max_candidates = collections.deque()

    def enqueue(self, x: int) -> None:
        self.data.append(x)
        while self.max_candidates and self.max_candidates[-1] < x:
            self.max_candidates.pop()
        self.max_candidates.append(x)

    def dequeue(self) -> int:
        val = self.data.popleft()
        if val == self.max_candidates[0]:
            self.max_candidates.popleft()
        return val

    def max(self) -> int:
        return self.max_candidates[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == "QueueWithMax":
                q = QueueWithMax()
            elif op == "enqueue":
                q.enqueue(arg)
            elif op == "dequeue":
                result = q.dequeue()
                if result != arg:
                    raise TestFailure(
                        "Dequeue: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "max":
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result)
                    )
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure("Unexpected IndexError exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "queue_with_max.py", "queue_with_max.tsv", queue_tester
        )
    )
