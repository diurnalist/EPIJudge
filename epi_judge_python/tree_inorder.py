from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    nodes = []
    processing = [(tree, False)]
    while processing:
        node, left_visited = processing.pop()
        if not node:
            continue
        if left_visited:
            nodes.append(node.data)
        else:
            # LIFO queue... put left branch on last so it's visited first, this lets
            # us ensure that when this node is processed we know we should add it to
            # the result.
            processing.append((node.right, False))
            processing.append((node, True))
            processing.append((node.left, False))
    return nodes


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_inorder.py", "tree_inorder.tsv", inorder_traversal
        )
    )
