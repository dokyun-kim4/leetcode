# kth Smallest Element in a BST

from binary_tree import *


def answer(root: TreeNode, k: int):
    path = []

    def dfs(node):
        if not node:
            return
        else:
            dfs(node.left)
            path.append(node.val)
            dfs(node.right)

    dfs(root)
    return path[k - 1]


if __name__ == "__main__":
    root = [3, 1, 4, None, 2]
    k = 1
    root = to_binary_tree(root)
    print(answer(root, k))
