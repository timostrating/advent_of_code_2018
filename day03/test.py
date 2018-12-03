import re

data = open("input.txt", "r")

claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)  # Nicer way of getting the data, Source https://www.reddit.com/r/adventofcode/comments/a2lesz/2018_day_3_solutions/

for i in claims:
    print(list(i))