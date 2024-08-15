# Valid perfect square


def answer(num):

    l = 0
    r = num

    while l <= r:

        m = (l + r) // 2

        if m * m == num:
            return True
        elif m * m > num:
            r = m - 1
        else:
            l = m + 1

    return False


if __name__ == "__main__":
    target = 48
    print(answer(target))
