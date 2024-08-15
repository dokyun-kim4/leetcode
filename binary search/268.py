# Problem 268: Missing Number


def answer(nums):

    # --------------- O(n) memory ------------------ #
    # soln = [i for i in range(len(nums) + 1)]
    # for num in soln:
    #     if num not in nums:
    #         return num

    # ---------------O(1) memory (with XOR) -------- #
    # ans = 0
    # for num in nums:
    #     ans ^= num
    # for num in range(len(nums) + 1):
    #     ans ^= num
    # return ans

    # ---------------O(1) memory (with sum) -------- #
    return sum([i for i in range(len(nums) + 1)]) - sum(nums)


if __name__ == "__main__":
    nums = [1, 2]
    print(answer(nums))
