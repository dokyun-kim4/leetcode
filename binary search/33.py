# Search in Rotated Sorted Array


def answer(nums: list[int], target: int):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) >> 1
        if nums[m] == target:
            return m

        if nums[m] >= nums[l]:  # in left sorted
            if target < nums[l] or target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        else:  # in right sorted
            if target > nums[r] or target < nums[m]:
                r = m - 1
            else:
                l = m + 1

    return -1


if __name__ == "__main__":
    nums = [1, 3]
    target = 3
    print(answer(nums, target))
