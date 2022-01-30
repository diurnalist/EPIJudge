import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    if not l0 or not l1:
        return None

    def llen(node):
        l = 0
        while node:
            node, l = node.next, l + 1
        return l

    l0len, l1len = llen(l0), llen(l1)
    longer = l0 if l0len > l1len else l1
    shorter = l0 if l0 is not longer else l1

    for _ in range(abs(l0len - l1len)):
        longer = longer.next

    while longer is not shorter:
        longer, shorter = longer.next, shorter.next
    return longer


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure("Invalid result")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "do_terminated_lists_overlap.py",
            "do_terminated_lists_overlap.tsv",
            overlapping_no_cycle_lists_wrapper,
        )
    )
