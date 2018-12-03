import numpy as np
# np.set_printoptions(threshold=np.inf)

data = open("input.txt", "r")
# data = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]

non_overlapped_ids = []
mask = np.zeros((999, 999), dtype=int)
overlaps = 0
for l in data:
    la = l.split(" ")
    x_start = int(la[2].replace(":", "").split(",")[1])
    x_end = x_start + int(la[3].split("x")[1])
    y_start = int(la[2].replace(":", "").split(",")[0])
    y_end = y_start + int(la[3].split("x")[0])

    overlapped = False
    for x in range(x_start, x_end):
        for y in range(y_start, y_end):
            if mask[y][x] == 0:
                mask[y][x] = int(la[0].replace("#", ""))
            elif mask[y][x] > 0:
                if mask[y][x] in non_overlapped_ids:
                    non_overlapped_ids.remove(mask[y][x])
                mask[y][x] = -1
                overlaps += 1
                overlapped = True
            else:
                overlapped = True

    if not overlapped:
        non_overlapped_ids.append(int(la[0].replace("#", "")))

print(mask, overlaps, non_overlapped_ids)