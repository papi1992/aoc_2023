from collections import defaultdict
from functools import reduce


with open("input.txt", "r") as input_file:
    data = input_file.read().splitlines()


scratchcards = defaultdict(int)
for line in data:
    play_no, numbers = line.split(":")
    _, play_no = play_no.replace(" ", "").split("Card")
    play_no = int(play_no)

    winning_numbers, my_numbers = numbers.split("|")
    winning_numbers, my_numbers = set(winning_numbers.strip().split(" ")), set(my_numbers.strip().split(" "))

    for _set in [winning_numbers, my_numbers]:
        try:
            _set.remove("")
        except KeyError:
            pass

    winning_numbers_section = winning_numbers.intersection(my_numbers)

    if play_no not in scratchcards:
        scratchcards[play_no] = 1
    else: 
        scratchcards[play_no] += 1


    scratchcards_rising = [_ for _ in range(play_no + 1, play_no + 1 + len(winning_numbers_section))]
    for rising_play_no in scratchcards_rising:
        scratchcards[rising_play_no] += scratchcards[play_no]

print(sum(_ for _ in scratchcards.values()))
