with open("input.txt", "r") as input_file:
    data = input_file.read().splitlines()

_, times = data[0].split(":")
times = [int(time) for time in times.strip().split(" ") if time]

_, distances = data[1].split(":")
distances = [int(distance) for distance in distances.strip().split(" ") if distance]

final_res = 1
for race_index, time in enumerate(times):

    total_ways_of_beat = 0
    for speed in range(1, time + 1):
        if distances[race_index] < (time-speed) * speed:
            total_ways_of_beat += 1
    
    final_res *= total_ways_of_beat


print(f"{times=}, {distances=}, {final_res=}")