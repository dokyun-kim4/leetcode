# Find First and Last Position of Element in Sorted Array


def upper(nums, target):
    i = -1
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) >> 1
        if target > nums[m]:
            l = m + 1
        elif target < nums[m]:
            r = m - 1
        else:
            i = m
            l = m + 1

    return i


def lower(nums, target):
    i = -1
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) >> 1
        if target > nums[m]:
            l = m + 1
        elif target < nums[m]:
            r = m - 1
        else:
            i = m
            r = m - 1

    return i


def answer(nums: list[int], target: int):
    return [lower(nums, target), upper(nums, target)]


if __name__ == "__main__":
    print(upper([0, 1, 1, 1], 1))
