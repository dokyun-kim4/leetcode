# Two Sum


def answer(nums: list[int], target: int):
    num2rem = {}

    for i, num in enumerate(nums):
        if target - num in num2rem:
            return [i, num2rem[target - num]]
        else:
            num2rem[num] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(answer(nums, target))
