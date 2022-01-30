from list_node import ListNode
from test_framework import generic_test

def reverse_list(head: ListNode) -> ListNode:
    dummy = ListNode()
    while head:
        dummy.next, head.next, head = head, dummy.next, head.next
    return dummy.next

def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # find the midpoint
    slow = fast = L
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    fwd, rev = L, reverse_list(slow)
    while fwd and rev:
        if fwd.data != rev.data:
            return False
        fwd, rev = fwd.next, rev.next
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
