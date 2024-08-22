# Majority Element


def answer(nums: list[int]):
    res = 0
    for num in nums:
        res ^= num

    return res


if __name__ == "__main__":
    nums = [1, 4, 1, 2, 2]
    print(answer(nums))
