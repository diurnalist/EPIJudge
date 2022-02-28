from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    prev, nodes = None, []
    while tree:
        if prev is tree.parent:
            if tree.left:
                next = tree.left
            else:
                nodes.append(tree.data)
                next = tree.right or tree.parent
        elif prev is tree.left:
            nodes.append(tree.data)
            next = tree.right or tree.parent
        else:
            next = tree.parent
        prev, tree = tree, next
    return nodes


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_with_parent_inorder.py",
            "tree_with_parent_inorder.tsv",
            inorder_traversal,
        )
    )
