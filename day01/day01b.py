data = list(open("input.txt", "r"))

def find_first_duplicate():
    old_frequencies = [0]
    input_index = 0

    while True:
        next = old_frequencies[-1] + int(data[input_index])

        if next in old_frequencies:
            return next
        else:
            old_frequencies.append(next)

        input_index += 1
        input_index %= data.__len__()


print("First duplicate:", find_first_duplicate() )
