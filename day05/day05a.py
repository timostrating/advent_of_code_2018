data = str(list(open("input.txt", "r"))[0])
data = list(data)

index = 0
while data[index] != "\n":
    if (data[index].upper() == data[index + 1] and data[index] != data[index + 1]) or (data[index + 1].upper() == data[index] and data[index + 1] != data[index]):
        del data[index:index+2]
        index -= 9
        if index < 0:
            index = -1

    index += 1

print(data.__len__() -1)
print("".join(data))
