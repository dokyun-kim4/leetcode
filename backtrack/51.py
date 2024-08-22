# N-Queens


def answer(n: int):
    colSet = set()
    downDiag = set()  # \
    upDiag = set()  # /

    res = []
    board = [["."] * n for _ in range(n)]

    def solveQueens(r: int):
        if r == n:
            res.append(["".join(row) for row in board])
            return

        else:
            for c in range(n):
                if (c in colSet) or (r - c in downDiag) or (r + c in upDiag):
                    continue
                else:
                    colSet.add(c)
                    downDiag.add(r - c)
                    upDiag.add(r + c)
                    board[r][c] = "Q"
                    solveQueens(r + 1)
                    colSet.remove(c)
                    downDiag.remove(r - c)
                    upDiag.remove(r + c)
                    board[r][c] = "."

    solveQueens(0)
    return res


if __name__ == "__main__":
    n = 4
    print(answer(n))
