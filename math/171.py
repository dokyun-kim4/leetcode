# Excel Sheet Column Number


def answer(columnTitle):

    columnNumber = 0

    for i, letter in enumerate(columnTitle[::-1]):

        columnNumber += ((ord(letter)) - 64) * (26**i)

    return columnNumber


if __name__ == "__main__":
    columnTitle = "AB"
    print(answer(columnTitle))
