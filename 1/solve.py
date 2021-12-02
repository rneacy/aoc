from pathlib import Path
import sys

if len(sys.argv) > 1:
    p = sys.argv[1]
else:
    p = "input"

with open(Path(__file__).parent.joinpath(p), "r") as inp:
    puzzle = [int(l) for l in inp.readlines()]

def part_a():
    res = 0
    for i in range(1, len(puzzle)):
        if puzzle[i] > puzzle[i-1]:
            res += 1

    print(res)

def part_b():
    res = 0
    i = 1
    prev = -1
    while i < len(puzzle) - 2:
        next = puzzle[i] + puzzle[i+1] + puzzle[i+2]
        if next > prev:
            res+=1
        prev=next
        i+=1

    print(res)

part_b()