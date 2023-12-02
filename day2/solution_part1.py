from typing import Dict, List, Tuple

max_numbers_of_cubes = {"red": 12, "green": 13, "blue": 14}

with open("input.txt", "r") as input_file:
    line_of_text = input_file.read().splitlines()


def parse(line: str) -> Tuple[str, List[Dict[str, int]]]:
    game, records = line.split(":")
    game_no = int(game.split(" ")[1])
    subsets_of_cubes = records.split(";")

    sets_of_cubes = []
    for subset in subsets_of_cubes:
        number_with_color_list = subset.split(",")

        _set = {}
        for number_with_color in number_with_color_list:
            number, color = number_with_color.strip().split(" ")
            _set[color] = int(number)

        sets_of_cubes.append(_set)

    return game_no, sets_of_cubes


def validate(sets_of_cubes: List[Dict[str, int]]) -> bool:
    for _set in sets_of_cubes:
        for color, number in _set.items():
            if max_numbers_of_cubes[color] < number:
                return False
            
    return True


sum = 0
for line in line_of_text:
    game_no, sets_of_cubes = parse(line)

    if validate(sets_of_cubes):
        sum += int(game_no)
    

print(sum)
