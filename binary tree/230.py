# kth Smallest Element in a BST

from binary_tree import *


def answer(root: TreeNode, k: int):
    res = None

    def dfs(node):
        nonlocal res
        nonlocal k
        if not node:
            return
        else:

            dfs(node.left)
            k -= 1
            if k == 0:
                res = node.val
            if k > 0:
                dfs(node.right)

    dfs(root)
    return res


if __name__ == "__main__":
    root = [3, 1, 4, None, 2]
    k = 2
    root = to_binary_tree(root)
    print(answer(root, k))
