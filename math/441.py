# Arranging Coins


def answer(n):

    # 1+2+3+4+ ... + k < n

    k = (2 * n + 0.25) ** 0.5 - 0.5
    return int(k)


if __name__ == "__main__":
    n = 5
    print(answer(n))
