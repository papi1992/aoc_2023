from collections import defaultdict
import re

pattern = "(\d+)"

with open("input.txt", "r") as input_file:
    data = input_file.read().splitlines()


gears = defaultdict(list)
def append_to_gears(line_index: int, line_part_gear_index: int, part_number: int):
    gears[f"{line_index}-{line_part_gear_index}"].append(part_number)


def before_number_is_gear(line_index: int, line: str, start_index: int, part_number: int) -> bool:
    if start_index > 0:
        start_index -= 1

    line_part = line[start_index]

    if line_part.count("*") > 0:
        append_to_gears(line_index, line[:start_index+1].rindex('*'), part_number)


def after_number_is_gear(line_index: int, line: str, end_index: int, part_number: int) -> bool:
    try:
        line_part = line[end_index]
        if line_part.count("*") > 0:
            append_to_gears(line_index, line[:end_index+1].rindex('*'), part_number)
    except IndexError:
        return


def above_number_there_is_gear(
        line_index: int, above_line: str, start_index: int, end_index: int, part_number: int
    ) -> bool:
    if start_index > 0:
        start_index -= 1

    line_part = above_line[start_index:end_index + 1]
    if line_part.count("*") > 0:
        append_to_gears(line_index, above_line[:end_index + 1].rindex('*'), part_number)


def under_number_there_is_gear(line_index: int, under_line: str, start_index: int, end_index: int, part_number: int) -> bool:
    if start_index > 0:
        start_index -= 1

    line_part = under_line[start_index:end_index + 1]
    if line_part.count("*") > 0:
        append_to_gears(line_index, under_line[:end_index + 1].rindex('*'), part_number)


sum = 0
for line_index, line in enumerate(data):
    for hit in re.finditer(pattern, line):
        part_number, start_index, end_index = int(hit.group()), int(hit.start()), int(hit.end())

        before_number_is_gear(line_index, line, start_index, part_number)
        after_number_is_gear(line_index, line, end_index, part_number)

        
        before_line = data[line_index - 1] if line_index > 0 else data[line_index]
        above_number_there_is_gear(line_index - 1, before_line, start_index, end_index, part_number)

        try:
            next_line = data[line_index + 1]
            under_number_there_is_gear(line_index + 1, next_line, start_index, end_index, part_number)
        except IndexError:
            pass

for gear_set in gears.values():
    if len(gear_set) == 2:
        sum += gear_set[0] * gear_set[1]

print(sum)
