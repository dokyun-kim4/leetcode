# Convert Sorted Array to Binary Search Tree

from binary_tree import *


def answer(nums: list[int]):

    def buildTree(l, r):

        if l > r:
            return None

        m = (l + r) >> 1
        root = TreeNode(nums[m])
        root.left = buildTree(l, m - 1)
        root.right = buildTree(m + 1, r)
        return root

    return buildTree(0, len(nums) - 1)


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    print_tree_as_list(answer(nums))
