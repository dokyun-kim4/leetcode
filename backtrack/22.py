# Generate Parentheses


def answer(n):
    res = []

    def backtrack(curStr, open, closed):
        print(curStr)
        if open == n and closed == n:
            res.append(curStr)
            return
        else:
            if open == n:
                backtrack(curStr + ")", open, closed + 1)
            elif open == closed:
                backtrack(curStr + "(", open + 1, closed)
            else:
                backtrack(curStr + ")", open, closed + 1)
                backtrack(curStr + "(", open + 1, closed)

    backtrack("(", 1, 0)
    return res


if __name__ == "__main__":
    n = 3
    print(answer(n))
