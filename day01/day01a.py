f = open("input.txt", "r")

cur_frequency = 0
for x in f:
    cur_frequency += int(x)

print(cur_frequency)
