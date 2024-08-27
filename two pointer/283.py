# Move Zeroes


def answer(nums):
    zero = 0
    real = 0

    while real < len(nums):
        if real > zero:

            if nums[zero] == 0 and nums[real] == 0:
                real += 1
                continue
            elif nums[zero] == 0:
                temp = nums[zero]
                nums[zero] = nums[real]
                nums[real] = temp
            zero += 1
            real += 1

        else:
            real += 1
    return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print(answer(nums))
