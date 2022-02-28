import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    # because a preorder always fills in the left subtree first,
    # we can create a simple solution that uses an iterator. the
    # iterator lets us immediately move on to the right subtree
    # due to the order in which arguments are evaluated.
    def build(i):
        x = next(i)
        if not x:
            return None
        return BinaryTreeNode(x, build(i), build(i))

    return build(iter(preorder))


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == "null" else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_from_preorder_with_null.py",
            "tree_from_preorder_with_null.tsv",
            reconstruct_preorder_wrapper,
        )
    )
