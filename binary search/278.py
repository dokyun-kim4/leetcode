# First Bad Version

firstBadVersion = 4


def isBadVersion(version):
    return version >= firstBadVersion


def answer(n):

    l = 1
    r = n

    while l <= r:

        m = (l + r) // 2

        if isBadVersion(m):
            if not isBadVersion(m - 1):
                return m
            else:
                r = m - 1

        else:
            l = m + 1


if __name__ == "__main__":

    n = 5
    print(answer(n))
