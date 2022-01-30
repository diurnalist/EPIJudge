from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    if not L:
        return None

    k_iter = L
    for _ in range(k):
        k_iter = k_iter.next

    i = dummy_head = ListNode(0, L)
    while k_iter:
        i = i.next
        k_iter = k_iter.next

    i.next = i.next.next
    return dummy_head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "delete_kth_last_from_list.py",
            "delete_kth_last_from_list.tsv",
            remove_kth_last,
        )
    )
