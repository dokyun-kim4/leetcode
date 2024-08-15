# Find intersection of 2 arrays


def answer(nums1, nums2):

    # ------ for loop ----- #
    # set1 = list(set(nums1))
    # set2 = list(set(nums2))
    # intersection = []

    # for num in set1:
    #     if num in set2:
    #         intersection.append(num)

    # return intersection

    # ------ intersection() ---- #
    set1 = set(nums1)
    set2 = set(nums2)

    return list(set1 & set2)


if __name__ == "__main__":
    l1 = [4, 9, 5]
    l2 = [9, 4, 9, 8, 4]

    print(answer(l1, l2))
