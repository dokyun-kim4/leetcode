# Find Minimum in Rotated Sorted Array


def answer(nums: list[int]):
    res = nums[0]

    l = 0
    r = len(nums) - 1

    while l <= r:

        if nums[r] > nums[l]:
            res = min(nums[l], res)
            break

        m = (l + r) >> 1
        res = min(nums[m], res)
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return res


if __name__ == "__main__":
    nums = [5, 1, 2, 3, 4]
    print(answer(nums))
