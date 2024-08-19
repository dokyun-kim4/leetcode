# Median of Two Sorted Arrays


def answerBinarySearch(nums1, nums2):
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A

    l, r = 0, len(A) - 1
    while True:
        i = (l + r) >> 1  # for A
        j = half - i - 2  # for B

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if i + 1 < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if j + 1 < len(B) else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:

            # odd
            if total % 2:
                return min(Aright, Bright)
            # even
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1


def answerTwoPointer(nums1, nums2):
    n, m = len(nums1), len(nums2)
    isEven = (n + m) % 2 == 0
    midIdx = (n + m) // 2
    nums = []

    l, r = 0, 0

    while l < n and r < m:

        if nums1[l] > nums2[r]:
            nums.append(nums2[r])
            r += 1
        elif nums1[l] < nums2[r]:
            nums.append(nums1[l])
            l += 1
        else:
            nums.append(nums2[r])
            nums.append(nums2[r])
            r += 1
            l += 1

    if l == n:
        nums += nums2[r::]
    elif r == m:
        nums += nums1[l::]

    if isEven:
        return (nums[midIdx] + nums[midIdx - 1]) / 2
    else:
        return nums[midIdx]


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(answerBinarySearch(nums1=nums1, nums2=nums2))
