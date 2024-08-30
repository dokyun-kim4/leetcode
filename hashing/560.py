# Subarray Sum Equals K


def answer(nums, k):
    prefSum = {}
    cumSum = 0
    count = 0

    for num in nums:

        prefSum += num
        if cumSum - k in prefSum:
            count += prefSum[cumSum - k]

        if cumSum in prefSum:
            prefSum[cumSum] += 1
        else:
            prefSum[cumSum] = 1
    return count
