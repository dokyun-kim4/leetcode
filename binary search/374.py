# Guess Number Higher or Lower


def guess(num):
    answer = 6
    if num == answer:
        return 0
    elif num > answer:
        return -1
    else:
        return 1


def answer(n):

    l = 0
    r = n

    while l <= r:
        m = (l + r) >> 1
        api_result = guess(m)

        match api_result:
            case 0:
                return m
            case -1:
                r = m - 1
            case 1:
                l = m + 1


if __name__ == "__main__":
    n = 10
    print(answer(n))
