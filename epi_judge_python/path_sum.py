from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    if not tree:
        return False
    remaining_weight -= tree.data
    if not (tree.left or tree.right):
        return not remaining_weight
    return has_path_sum(tree.left, remaining_weight) or has_path_sum(
        tree.right, remaining_weight
    )


if __name__ == "__main__":
    exit(generic_test.generic_test_main("path_sum.py", "path_sum.tsv", has_path_sum))
