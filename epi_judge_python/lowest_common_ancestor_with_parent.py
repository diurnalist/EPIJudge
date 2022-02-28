import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    def depth(node: BinaryTreeNode) -> int:
        d = 0
        while node.parent:
            d, node = d + 1, node.parent
        return d

    d0, d1 = depth(node0), depth(node1)
    if d0 > d1:
        for _ in range(abs(d0 - d1)):
            node0 = node0.parent
    elif d1 > d0:
        for _ in range(abs(d0 - d1)):
            node1 = node1.parent
    # at this point both nodes have the same depth
    while node0:
        if node0 is node1:
            return node0
        node0, node1 = node0.parent, node1.parent


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0), must_find_node(tree, node1))
    )

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_with_parent.py",
            "lowest_common_ancestor.tsv",
            lca_wrapper,
        )
    )
