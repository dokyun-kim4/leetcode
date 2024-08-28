# Group Anagrams


def answer(strs: list[str]):
    res = {}
    for word in strs:

        word_sorted = "".join(sorted(list(word)))

        if word_sorted in res:
            res[word_sorted].append(word)
        else:
            res[word_sorted] = [word]

    return list(res.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(answer(strs))
