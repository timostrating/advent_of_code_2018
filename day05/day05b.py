data = str(list(open("input.txt", "r"))[0])
# data = "dabAcCaCBAcCcaDA\n"

def reduce(data_string):
    index = 0
    data = list(data_string.split("\n")[0])
    data.append("\n")
    while data[index] != "\n":
        if (data[index].upper() == data[index + 1] and data[index] != data[index + 1]) or (
                data[index + 1].upper() == data[index] and data[index + 1] != data[index]):
            del data[index:index + 2]
            index -= 9
            if index < 0:
                index = -1

        index += 1

    return ("".join(data)).replace("\n", "")


data = reduce(data)
start_score = data.__len__()
min_score = ("?", 99999)
for c in "abcdefghijklmnopqrstuvwxyz":
    new_data = data[:]
    new_data = ("".join(new_data)).replace(c, "").replace(c.upper(), "")
    new_data = reduce(new_data)

    score = new_data.__len__()
    if score < min_score[1]:
        min_score = (c, score)
    print(c, score)


print("min score: ", min_score)
