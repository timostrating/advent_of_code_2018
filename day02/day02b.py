# d = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
d = list(open("input.txt", "r"))


def levenshtein_distance(s, t):  # https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance
    """
    calculates the levenstein distance between 2 strings. This is the number of characters that the 2 strings differ
    from each other.
    """
    v0 = [None] * (len(t) + 1)
    v1 = [None] * (len(t) + 1)

    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]

    return v1[len(t)]


d.sort()
for l_index in range(0, d.__len__() - 1):
    if levenshtein_distance(d[l_index], d[l_index + 1]) == 1:
        for i, c in enumerate(d[l_index]):
            if c in d[l_index + 1][i]:
                print(c, end="")
