from string import digits
import re

digit_names_with_values = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
digit_names = list(digit_names_with_values.keys())
pattern = f"(?=(\d)|{'|'.join([f'({digit_name})' for digit_name in digit_names])})"

with open("input.txt", "r") as input_file:
    lines_of_text = input_file.read().splitlines()

sum = 0
for line in lines_of_text:

    calibration_values = []
    results = [result for result in re.findall(pattern, line)]
    for hit in  [hit for result in results for hit in result if hit]:
        if hit not in digits:
            calibration_values.append(digit_names_with_values[hit])
        else:
            calibration_values.append(hit)


    if len(calibration_values) == 1:
        sum += int(f"{calibration_values[0]}{calibration_values[0]}")
        continue
    
    sum += int(f"{calibration_values[0]}{calibration_values[-1]}")
    print(f"{calibration_values[0]}{calibration_values[-1]}")
        
print(sum)

    

