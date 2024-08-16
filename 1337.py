# The K Weakest Rows in a Matrix


def binarySum(row):
    l = 0
    r = len(row) - 1

    if row[-1]:
        return r + 1
    if not row[0]:
        return l

    while l <= r:
        m = (l + r) >> 1

        if not row[m]:
            if row[m - 1]:
                return m
            else:
                r = m - 1
        else:
            l = m + 1


def answer(mat, k):

    soldiers = [(i, binarySum(row)) for i, row in enumerate(mat)]
    soldiers.sort(key=lambda x: x[1])
    return [i[0] for i in soldiers[0:k]]


if __name__ == "__main__":
    mat = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
    ]
    k = 3

    print(answer(mat, k))
