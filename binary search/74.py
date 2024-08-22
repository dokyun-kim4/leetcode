# Search a 2D Matrix


def answer(matrix: list[list[int]], target: int):
    m, n = len(matrix), len(matrix[0])

    l, r = 0, m * n - 1

    while l <= r:
        m = (l + r) >> 1
        mi, mj = m // n, m % n

        midNum = matrix[mi][mj]

        if midNum == target:
            return True
        else:
            if midNum > target:
                r = m - 1
            else:
                l = m + 1
    return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20]]
    target = 3
    print(answer(matrix, target))
