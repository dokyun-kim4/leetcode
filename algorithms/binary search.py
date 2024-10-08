def binarySearch(arr: list, target: int):

    l = 0
    r = len(arr) - 1

    while l <= r:

        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1

    return -1


lst = [1, 3, 5, 7, 8, 9]
target = 9

print(binarySearch(lst, 1))
