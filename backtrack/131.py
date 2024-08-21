# Palindrome Partitioning


def answer(s: str):
    res = []

    def backtrack(remStr, subStr):
        if len(remStr) == 0:
            res.append(subStr.copy())
            return
        else:
            for i in range(1, len(remStr) + 1):
                curSub = remStr[0:i]
                if curSub == curSub[::-1]:
                    backtrack(remStr[i::], subStr + [curSub])
                else:
                    continue

    backtrack(s, [])
    return res


if __name__ == "__main__":
    s = "aab"
    print(answer(s))
