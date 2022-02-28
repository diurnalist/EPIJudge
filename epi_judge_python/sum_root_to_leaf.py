from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def subtree_sum(tree, sum_at_level):
        if not tree:
            return 0
        sum_at_level = (sum_at_level * 2) + tree.data
        if not (tree.left or tree.right):
            return sum_at_level
        return subtree_sum(tree.left, sum_at_level) + subtree_sum(
            tree.right, sum_at_level
        )

    return subtree_sum(tree, 0)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", "sum_root_to_leaf.tsv", sum_root_to_leaf
        )
    )
