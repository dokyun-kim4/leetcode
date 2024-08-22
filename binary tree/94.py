# Binary Tree Inorder Traversal

from binary_tree import *


def answer(root: TreeNode):
    path = []

    def dfs(node):
        if not node:
            return
        else:
            dfs(node.left)
            path.append(node.val)
            dfs(node.right)

    dfs(root)
    return path


if __name__ == "__main__":
    root = to_binary_tree([1, None, 2, 3])
    print(answer(root))
