from string import digits


with open("input.txt", "r") as input_file:
    lines_of_text = input_file.read().splitlines()

sum = 0
for line in lines_of_text:
    calibration_values = [char for char in line if char in digits]

    if len(calibration_values) == 1:
        sum += int(f"{calibration_values[0]}{calibration_values[0]}")
        continue
    
    sum += int(f"{calibration_values[0]}{calibration_values[-1]}")
        
print(sum)
