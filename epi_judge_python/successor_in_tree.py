import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # if there is a right subtree, the successor is easy.
    # is is the leftmost node in that subtree.
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node

    # in this situation:
    #
    #        o
    #       /
    #      o
    #       \
    #        o
    #         \
    #          o <-
    #
    # there is no right branch. the successor in this
    # case is the root node. generally, it is a parent
    # that has this node in its _left_ subtree. we can
    # stop when we have gotten out of a right subtree
    # (i.e., stopped riding the right "rail")
    while node.parent and node.parent.right is node:
        node = node.parent
    return node.parent


@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "successor_in_tree.py", "successor_in_tree.tsv", find_successor_wrapper
        )
    )
