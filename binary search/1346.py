# Check If N and Its Double Exist


def answer(arr):
    arr.sort()

    for i, num in enumerate(arr):

        l = 0
        r = len(arr) - 1
        target = num * 2

        while l <= r:
            m = (l + r) >> 1

            if arr[m] == target and i != m:
                return True
            elif arr[m] > target:
                r = m - 1
            else:
                l = m + 1

    return False


if __name__ == "__main__":
    arr = [10, 2, 5, 3]
    print(answer(arr))
