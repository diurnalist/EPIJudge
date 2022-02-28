from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(
    preorder: List[int], inorder: List[int]
) -> BinaryTreeNode:
    in_idx = {data: i for i, data in enumerate(inorder)}

    def build(pre_start, pre_end, in_start, in_end):
        if pre_end <= pre_start or in_end <= in_start:
            return None
        # the preorder visits root, then left then right. so root is always the first
        # element of any preorder. we look up where that element is in the inorder list.
        root_in_idx = in_idx[preorder[pre_start]]
        # distance from the root node to where the inorder sublist starts == the size
        # of the entire left branch (b/c inorder visits root last.)
        l_size = root_in_idx - in_start
        # so, we know the root == preorder[pre_start].
        return BinaryTreeNode(
            preorder[pre_start],
            # and we can prune the preorder and inorder subtrees as follows:
            # for l branch, preorder = the next entry and for the next 'l_size' nodes.
            #               inorder = same entry, up to root
            # for r branch, preorder = right after preorder, to end
            #               inorder = right after inorder, and past root, to end
            build(pre_start + 1, pre_start + 1 + l_size, in_start, root_in_idx),
            build(pre_start + 1 + l_size, pre_end, root_in_idx + 1, in_end),
        )

    return build(0, len(preorder), 0, len(inorder))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_from_preorder_inorder.py",
            "tree_from_preorder_inorder.tsv",
            binary_tree_from_preorder_inorder,
        )
    )
