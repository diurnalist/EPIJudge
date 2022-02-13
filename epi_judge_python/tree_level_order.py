from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    # for each root of the subtree
    # store the data in the current depth key list
    # get new list of roots
    if not tree:
        return []
    ordering = []
    current_level = [tree]
    while current_level:
        ordering.append([n.data for n in current_level])
        current_level = [
            branch for n in current_level for branch in (n.left, n.right) if branch
        ]
    return ordering


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_level_order.py", "tree_level_order.tsv", binary_tree_depth_order
        )
    )
