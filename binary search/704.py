# Binary Search


def answer(nums, target):

    l = 0
    r = len(nums) - 1

    while l <= r:

        m = (l + r) >> 1

        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    print(answer(nums=nums, target=target))
