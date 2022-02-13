from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # Check that left branch doesn't have height greater than other branch (plus 1)
    def _subtree_height(node: BinaryTreeNode):
        if not node:
            return 0
        return 1 + max(_subtree_height(node.left), _subtree_height(node.right))

    print(_subtree_height(tree.left))
    print(_subtree_height(tree.right))
    return abs(_subtree_height(tree.left) - _subtree_height(tree.right)) <= 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_balanced.py", "is_tree_balanced.tsv", is_balanced_binary_tree
        )
    )
