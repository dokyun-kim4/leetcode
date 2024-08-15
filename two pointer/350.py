# Find intersection of 2 arrays II


def answer(nums1, nums2):

    nums1.sort()
    nums2.sort()
    soln = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):

        if nums1[i] == nums2[j]:
            soln.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1

    return soln


if __name__ == "__main__":

    n1 = [1, 2, 2, 1]
    n2 = [2, 3]

    print(answer(n1, n2))
