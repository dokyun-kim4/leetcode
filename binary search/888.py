# Fair candy swap


def answer(aliceSizes, bobSizes):

    aliceSizes.sort()
    bobSizes.sort()

    aliceSum = sum(aliceSizes)
    bobSum = sum(bobSizes)
    sum_target = (aliceSum + bobSum) >> 1

    for a_size in aliceSizes:

        need = sum_target - aliceSum
        swap_target = a_size + need

        l = 0
        r = len(bobSizes) - 1

        while l <= r:
            m = (l + r) >> 1
            b_size = bobSizes[m]
            if b_size == swap_target:
                if (aliceSum - a_size + b_size) == (bobSum - b_size + a_size):
                    return [a_size, b_size]
            elif b_size > swap_target:
                r = m - 1
            else:
                l = m + 1


if __name__ == "__main__":
    aliceSizes = [1, 1]
    bobSizes = [2, 2]

    print(answer(aliceSizes=aliceSizes, bobSizes=bobSizes))
