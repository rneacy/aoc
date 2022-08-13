from pathlib import Path
from math import floor, ceil
import sys

if len(sys.argv) > 1:
    p = sys.argv[1]
else:
    p = "input"

with open(Path(__file__).parent.joinpath(p), "r") as inp:
    puzzle = [l.rstrip() for l in inp.readlines()][0].split(",")
    puzzle = [int(n) for n in puzzle]
    puzzle.sort()

def part_a():
    med = puzzle[len(puzzle)//2]
    res = sum([abs(x - med) for x in puzzle])
    print(res)

def part_b():
    mean = sum(puzzle)/len(puzzle)
    mean = ceil(mean) if int(mean) % 2 == 0 else floor(mean)  # can't actually verify if this is true lol
    print(sum([sum([x for x in range(1, abs(current-mean) + 1)]) for current in puzzle]))

part_b()