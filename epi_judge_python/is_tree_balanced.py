from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import namedtuple

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    Check = namedtuple("Check", ["height", "balanced"])

    def _check(tree: BinaryTreeNode):
        if not tree:
            return Check(-1, True)
        left_branch = _check(tree.left)
        if not left_branch.balanced:
            return left_branch
        right_branch = _check(tree.right)
        if not right_branch.balanced:
            return right_branch
        return Check(
            max(left_branch.height, right_branch.height) + 1,
            abs(left_branch.height - right_branch.height) <= 1
        )

    return _check(tree).balanced


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_balanced.py", "is_tree_balanced.tsv", is_balanced_binary_tree
        )
    )
