# Word Search


def answer(board: list[str], word: str):
    m = len(board)
    n = len(board[0])

    path = set()

    def backtrack(row, col, i):
        if i == len(word):
            return True

        if (
            row < 0
            or col < 0
            or row >= m
            or col >= n
            or board[row][col] != word[i]
            or (row, col) in path
        ):
            return False

        else:
            path.add((row, col))

            res = (
                backtrack(row + 1, col, i + 1)
                or backtrack(row - 1, col, i + 1)
                or backtrack(row, col + 1, i + 1)
                or backtrack(row, col - 1, i + 1)
            )

            path.remove((row, col))
        return res

    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0):
                return True

    return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(answer(board, word))
