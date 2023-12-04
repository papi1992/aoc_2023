import re

pattern = "(\d+)"

with open("input.txt", "r") as input_file:
    data = input_file.read().splitlines()


def before_number_is_symbol(line: str, start_index: int) -> bool:
    if line[start_index - 1] == ".":
        return False
    return True


def after_number_is_symbol(line: str, end_index: int) -> bool:
    try:
        if line[end_index] == ".":
            return False
        return True
    except IndexError:
        return False


def above_number_there_is_symbol(before_number: str, start_index: int, end_index: int) -> bool:
    if start_index > 0:
        start_index -= 1

    try:
        if all(char == "." for char in before_number[start_index:end_index + 1]):
            return False
        return True
    except IndexError:
        pass

    if all(char == "." for char in before_number[start_index:end_index]):
        return False
    return True


def under_number_there_is_symbol(next_line: str, start_index: int, end_index: int) -> bool:
    if start_index > 0:
        start_index -= 1

    try:
        if all(char == "." for char in next_line[start_index:end_index + 1]):
            return False
        return True
    except IndexError:
        pass

    if all(char == "." for char in next_line[start_index:end_index]):
        return False
    return True


sum = 0
for line_index, line in enumerate(data):
    for hit in re.finditer(pattern, line):
        part_number, start_index, end_index = int(hit.group()), int(hit.start()), int(hit.end())

        if start_index > 0:
            if before_number_is_symbol(line, start_index):
                sum += part_number
                continue

        if after_number_is_symbol(line, end_index):
            sum += part_number
            continue

        
        if line_index > 0:
            before_line = data[line_index - 1]
            if above_number_there_is_symbol(before_line, start_index, end_index):
                sum += part_number
                continue

        try:
            next_line = data[line_index + 1]
            if under_number_there_is_symbol(next_line, start_index, end_index):
                sum += part_number
                continue
        except IndexError:
            continue

print(sum)
