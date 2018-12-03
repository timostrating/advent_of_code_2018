import numpy as np

data = open("input.txt", "r")
# data = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]


mask = np.zeros((999, 999), dtype=int)
overlaps = 0
for l in data:
    la = l.split(" ")
    x_start = int(la[2].replace(":", "").split(",")[1])
    x_end = x_start + int(la[3].split("x")[1])
    y_start = int(la[2].replace(":", "").split(",")[0])
    y_end = y_start + int(la[3].split("x")[0])

    for x in range(x_start, x_end):
        for y in range(y_start, y_end):
            if mask[y][x] == 0:
                mask[y][x] = int(la[0][1])
            elif mask[y][x] > 0:
                mask[y][x] = -1
                overlaps += 1


print(mask, overlaps)