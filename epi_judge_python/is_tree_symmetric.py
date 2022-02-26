from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    # symmetry means the right branch of the left == the left branch of the right,
    # and vice-versa.
    def _check(ltree: BinaryTreeNode, rtree: BinaryTreeNode):
        if not (ltree or rtree):
            return True
        elif not (ltree and rtree):
            return False
        return (
            ltree.data == rtree.data
            and _check(ltree.right, rtree.left)
            and _check(ltree.left, rtree.right)
        )

    return (not tree) or _check(tree.left, tree.right)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_symmetric.py", "is_tree_symmetric.tsv", is_symmetric
        )
    )
