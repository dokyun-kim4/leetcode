# Maximum Depth of Binary Tree

from binary_tree import *


def answer(root: TreeNode):
    curMax = 0

    def dfs(node, curDepth):
        nonlocal curMax
        if not node:
            curMax = max(curMax, curDepth)
            return

        else:
            dfs(node.left, curDepth + 1)
            dfs(node.right, curDepth + 1)

    dfs(root, 0)
    return curMax


if __name__ == "__main__":
    root = to_binary_tree([1, None, 2, 3])
    print(answer(root))
