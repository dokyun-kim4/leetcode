# Count Negative Numbers in a Sorted Matrix


def answer(grid):
    def countNegativeInRow(row):
        l = 0
        r = len(row) - 1

        if row[-1] >= 0:
            return 0
        elif row[0] < 0:
            return len(row)
        else:
            while l <= r:
                m = (l + r) >> 1

                if row[m] < 0:
                    if row[m - 1] >= 0:
                        return len(row) - m
                    else:
                        r = m - 1
                else:
                    l = m + 1

    negNum = 0
    for row in grid:
        negNum += countNegativeInRow(row)

    return negNum


if __name__ == "__main__":
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(answer(grid=grid))
