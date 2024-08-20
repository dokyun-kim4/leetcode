# Subsets


# My version
def answer(nums: list[int]):
    res = [[]]

    def backtrack(curLst, arr):
        res.append(curLst)
        for i, num in enumerate(arr):
            backtrack(curLst + [num], arr[i + 1 : :])

    for i in range(len(nums)):
        print(f"first calls {nums[i]}")
        backtrack([nums[i]], nums[i + 1 : :])
    return res


# dfs solution
def answerDfs(nums: list[int]):
    res = []

    subset = []

    def backtrack(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        # include nums[i]
        subset.append(nums[i])
        backtrack(i + 1)

        # not include nums[i]
        subset.pop()
        backtrack(i + 1)

    backtrack(0)
    return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(answer(nums))
