from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    head = sub_head = ListNode(0, L)
    for _ in range(1, start):
        sub_head = sub_head.next

    sub_iter = sub_head.next
    # .... | <-. . . . . . | .....
    for _ in range(start, finish):
        tmp = sub_iter.next
        # Skip over tmp
        sub_iter.next = tmp.next
        # Move tmp to the front of the sublist
        tmp.next, sub_head.next = sub_head.next, tmp

    return head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_sublist.py", "reverse_sublist.tsv", reverse_sublist
        )
    )
