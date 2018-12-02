from collections import Counter
from functools import reduce
from operator import mul

# d = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
d = open("input.txt", "r")
results = []

for l in d:
    ld = Counter(l)
    l_results = set()
    for k in ld:
        if ld[k] > 1:
            l_results.add(ld[k])

    print(l_results)
    if l_results.__len__() > 0:
        results.append(l_results)
    # counter += l_results.__len__()

flat_list = [item for sublist in results for item in sublist] # flatten our array of sets
print("checksum: ", reduce(mul, Counter(flat_list).values(), 1))