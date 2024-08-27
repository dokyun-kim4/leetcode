# Validate Binary Search Tree


from binary_tree import *


def answer(root: TreeNode):

    def bst(node, left, right):
        if not node:
            print("reached end")
            return True

        if node.val <= left or node.val >= right:
            return False

        return bst(node.left, left, node.val) and bst(node.right, node.val, right)

    res = bst(root, float("-infinity"), float("infinity"))
    return res


if __name__ == "__main__":
    root = [5, 4, 6, None, None, 3, 7]
    root = to_binary_tree(root)
    print(answer(root))
