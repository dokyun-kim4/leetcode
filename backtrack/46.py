# Permutations


def answer(nums):
    res = []
    n = len(nums)

    # using DFS
    def backtrack(visited, curLst):

        if len(curLst) == n:
            res.append(curLst)
            return
        else:
            for i, num in enumerate(nums):
                if visited[i]:
                    continue
                else:
                    visited[i] = True
                    backtrack(visited, curLst + [num])
                    visited[i] = False

    backtrack([False] * n, [])
    return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(answer(nums))
