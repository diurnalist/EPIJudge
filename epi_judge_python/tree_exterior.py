import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    if not tree:
        return []

    l_side, cur = [], tree.left
    while cur:
        l_side.append(cur)
        if cur.left:
            cur = cur.left
        else:
            cur = cur.right

    r_side, cur = [], tree.right
    while cur:
        r_side.append(cur)
        if cur.right:
            cur = cur.right
        else:
            cur = cur.left
    r_side = list(reversed(r_side))

    def leaves(subtree):
        if not subtree:
            return []
        elif not (subtree.left or subtree.right):
            return [subtree]
        return leaves(subtree.left) + leaves(subtree.right)

    return [tree] + l_side + leaves(tree.left)[1:] + leaves(tree.right) + r_side[1:]


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure("Resulting list contains None")
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_exterior.py", "tree_exterior.tsv", create_output_list_wrapper
        )
    )
