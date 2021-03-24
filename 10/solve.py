import copy
from pathlib import Path

with open(Path(__file__).parent.joinpath("test"), "r") as inp:
    puzzle = inp.readlines()
    puzzle = [int(line) for line in puzzle]
    puzzle.sort()
    puzzle.insert(0, 0)
    puzzle.append(max(puzzle) + 3)

print(puzzle)

compat_range = 3

def jolt_diffs():
    differences = [puzzle[i+1]-puzzle[i] for i in range(len(puzzle) - 1)]
    return differences.count(1) * differences.count(3)

def part_a():
    print(jolt_diffs())
