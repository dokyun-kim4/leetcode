# Binary Tree Level Order Traversal

from binary_tree import *


def answer(root: TreeNode):

    if root is None:
        return []

    visited = []
    queue = [root]

    while len(queue) > 0:
        levelLength = len(queue)
        curLevel = []
        for _ in range(levelLength):
            curNode = queue.pop(0)
            curLevel.append(curNode.val)
            if curNode.left is not None:
                queue.append(curNode.left)
            if curNode.right is not None:
                queue.append(curNode.right)
        visited.append(curLevel)
    return visited


if __name__ == "__main__":
    root = to_binary_tree([3, 9, 20, None, None, 15, 7])
    print(answer(root))
