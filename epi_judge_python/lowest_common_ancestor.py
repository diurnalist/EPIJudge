import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(
    tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode
) -> Optional[BinaryTreeNode]:
    def _path_to(root: BinaryTreeNode, search: BinaryTreeNode, path: list):
        if not root:
            return None
        path.append(root)
        if root.data == search.data:
            return path
        return _path_to(root.left, search, path.copy()) or _path_to(
            root.right, search, path.copy()
        )

    path_to_0 = _path_to(tree, node0, [])
    path_to_1 = _path_to(tree, node1, [])
    shorter = min(len(path_to_0), len(path_to_1))
    for i in range(1, shorter):
        if path_to_0[i] != path_to_1[i]:
            return path_to_0[i - 1]
        elif i == len(path_to_0) - 1:
            return path_to_0[-1]
        elif i == len(path_to_1) - 1:
            return path_to_1[-1]
    return tree


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(
            lca, tree, must_find_node(tree, key1), must_find_node(tree, key2)
        )
    )

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor.py", "lowest_common_ancestor.tsv", lca_wrapper
        )
    )
