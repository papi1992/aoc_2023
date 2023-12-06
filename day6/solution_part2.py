with open("input.txt", "r") as input_file:
    data = input_file.read().splitlines()

_, time = data[0].split(":")
time = int("".join(time.strip().split(" ")))

_, distance = data[1].split(":")
distance = int("".join(distance.strip().split(" ")))

final_res = 1
total_ways_of_beat = 0
for speed in range(1, time + 1):
    if distance < (time-speed) * speed:
        total_ways_of_beat += 1
    
final_res *= total_ways_of_beat


print(f"{time=}, {distance=}, {final_res=}")