# Excel Sheet Column Title


def answer(columnNumber):

    columnTitle = ""

    while columnNumber != 0:
        asc = (columnNumber - 1) % 26
        columnTitle += chr(asc + 65)
        columnNumber = (columnNumber - 1) // 26

    return columnTitle[::-1]


if __name__ == "__main__":
    columnNumber = 701
    print(answer(columnNumber))
    print(26 // 26)
