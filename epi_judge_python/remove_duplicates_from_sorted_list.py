from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    it = L
    while it:
        next_it = it.next
        while next_it and next_it.data == it.data:
            next_it = next_it.next
        it.next = next_it
        it = it.next
    return L


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            "remove_duplicates_from_sorted_list.tsv",
            remove_duplicates,
        )
    )
