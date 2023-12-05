with open("input.txt", "r") as input_file:
    data = input_file.read().splitlines()

seeds_line, data = data[0], data[1:]
_, seeds = seeds_line.split(":")
seeds = [int(seed) for seed in seeds.strip().split(" ")]


def is_between(previous_category_value: int, range_start: int, range_end: int) -> bool:
    return previous_category_value >= range_start and previous_category_value <= range_end

food_chain = [{"seed": seed} for seed in seeds]

for food_chain_element in food_chain:
    print("-" * 20)
    source_indicator = "seed"

    for line_index, line in enumerate(data[1:]):
        if "map" in line:
            previous_category_value = food_chain_element[source_indicator]

            indicators, _ = line.split(" ")
            source_indicator = indicators.split("-")[-1]

            food_chain_element[source_indicator] = previous_category_value
            continue

        try:
            destination_range_start, source_range_start, range_length = [int(value) for value in line.split(" ")]
        except ValueError:
            continue

        if is_between(previous_category_value, source_range_start, source_range_start + range_length - 1):
            food_chain_element[source_indicator] = previous_category_value + (destination_range_start - source_range_start)

        
        print(f"{source_indicator=} {previous_category_value=} {destination_range_start=} {source_range_start=} {range_length=}")

    print(food_chain_element)

print(min(fce["location"] for fce in food_chain))
