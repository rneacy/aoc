from pathlib import Path
import sys

if len(sys.argv) > 1:
    p = sys.argv[1]
else:
    p = "input"

with open(Path(__file__).parent.joinpath(p), "r") as inp:
    puzzle = [l.split(" ") for l in inp.readlines()]

def part_a():
    d, h = 0, 0
    for step in puzzle:
        if step[0] == "forward":
            h += int(step[1].rstrip())
        elif step[0] == "down":
            d += int(step[1].rstrip())
        else:
            d -= int(step[1].rstrip())

    print(d*h)

def part_b():
    d, h, a = 0, 0, 0
    for step in puzzle:
        val = int(step[1].rstrip())
        if step[0] == "forward":
            h += val
            d += (val * a)
        elif step[0] == "down":
            a += val
        else:
            a -= val

    print(d*h)

#part_a()
part_b()