# Longest Consecutive Sequence


def answer_nlogn(nums: list[int]):
    nums = sorted(nums)
    prevNum = None
    curLen = 0
    curMax = 0
    for num in nums:
        if prevNum is None:
            curLen += 1
        else:
            if num == prevNum:
                continue
            elif num - prevNum == 1:
                curLen += 1
            else:
                if curLen > curMax:
                    curMax = curLen
                curLen = 1
        prevNum = num

    return max(curLen, curMax)


def answer_n(nums: list[int]):
    numSet = set(nums)
    curMax = 0
    for num in numSet:
        if (num - 1) in numSet:
            continue
        else:
            count = 1
            while (num + 1) in numSet:
                count += 1
                num += 1
            if count > curMax:
                curMax = count

    return max(curMax, count)


if __name__ == "__main__":
    nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
    print(answer_n(nums))
