from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    even, odd = ListNode(), ListNode()
    even_head, odd_head = even, odd
    i, node = 0, L
    while node:
        if i % 2 == 0:
            even.next = node
            even = even.next
        else:
            odd.next = node
            odd = odd.next
        i, node = i + 1, node.next
    even.next = odd_head.next
    odd.next = None
    return even_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
