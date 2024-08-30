# Pascal Triangle


def answer(rows: int):
    res = [[1] * i for i in range(1, rows + 1)]
    if rows < 3:
        return res
    else:
        for i in range(2, rows):
            for j in range(1, i):
                res[i][j] = res[i - 1][j] + res[i - 1][j - 1]

    return res


print(answer(4))
