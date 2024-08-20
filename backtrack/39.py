# Combination Sum


def answer(candidates, target):
    res = []

    def backtrack(curSum, curLst, nums):
        for i, num in enumerate(nums):
            if curSum == target:
                res.append(curLst)
                return
            elif curSum > target:
                return
            else:
                backtrack(curSum + num, curLst + [num], nums[i::])
        return

    for i in range(len(candidates)):
        backtrack(candidates[i], [candidates[i]], candidates[i::])
    return res


if __name__ == "__main__":
    candidates = [2, 3, 5]
    target = 8
    print(answer(candidates=candidates, target=target))
