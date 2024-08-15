# Find Smallest Letter Greater Than Target


def answer(letters: list[str], target: str) -> str:

    l, r = 0, len(letters) - 1

    if letters[-1] <= target or letters[0] > target:
        return letters[0]

    while l <= r:
        m = (l + r) >> 1

        if letters[m] > target:
            r = m - 1
        else:
            l = m + 1

        print(l, r)

    return letters[l]


if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "c"
    print(answer(letters, target))
