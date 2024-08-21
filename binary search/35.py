# Search Insert Position


def answer(nums: list[int], target: int):
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) >> 1
        if nums[m] == target:
            return m
        else:
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
    return l


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 2
    print(answer(nums, target))
