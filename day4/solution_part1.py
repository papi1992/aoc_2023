from functools import reduce


with open("input.txt", "r") as input_file:
    data = input_file.read().splitlines()

sum = 0
for line in data:
    play_no, numbers = line.split(":")
    winning_numbers, my_numbers = numbers.split("|")
    winning_numbers, my_numbers = set(winning_numbers.strip().split(" ")), set(my_numbers.strip().split(" "))

    try:
        winning_numbers.remove("")
    except KeyError:
        pass

    try:
        my_numbers.remove("")
    except KeyError:
        pass

    winning_numbers_section = winning_numbers.intersection(my_numbers)

    if len(winning_numbers_section) == 0:
        sum += 0
    elif len(winning_numbers_section) == 1:
        sum += 1
    else:
        sum += pow(2, len(winning_numbers_section) - 1)

print(sum)
