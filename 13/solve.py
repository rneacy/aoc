from pathlib import Path
import numpy as np

with open(Path(__file__).parent.joinpath("input"), "r") as inp:
    puzzle = inp.readlines()
    puzzle = [l.rstrip() for l in puzzle]

    depart = int(puzzle[0])

def get_small(bus_time):
    rem = (depart + bus_time) % bus_time

    if rem == 0:
        return depart
    else:
        return (depart + bus_time - rem)

def part_a():
    buses = [int(x) for x in puzzle[1].split(',') if x != "x"]

    available = [get_small(bus) for bus in buses]
    earliest = np.argmin(available)
    wait_time = available[earliest] - depart

    return buses[earliest] * wait_time

def part_b(): # This was way too tricky
    preparse = puzzle[1].split(',')
    buses = [{"index": x, "id": int(preparse[x])} for x in range(len(preparse)) if preparse[x] != "x"]

    increment = buses[0]["id"]
    time = 0

    for bus in buses[1:]:
        while (time + bus["index"]) % bus["id"] != 0:
            time += increment

        increment *= bus["id"]

    return time

print(part_b())