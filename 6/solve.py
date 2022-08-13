from pathlib import Path
import sys

if len(sys.argv) > 1:
    p = sys.argv[1]
else:
    p = "input"

with open(Path(__file__).parent.joinpath(p), "r") as inp:
    puzzle = [l.rstrip() for l in inp.readlines()][0].split(",")
    puzzle = [int(n) for n in puzzle]

def part_a():
    global puzzle

    limit = 80

    while limit > 0:
        for i in range(len(puzzle)):
            if puzzle[i] == 0:
                puzzle[i] = 6
                puzzle.append(8)
                continue
            puzzle[i] -= 1

        limit -= 1
        
    print(len(puzzle))

def part_b_which_is_part_a_but_not_brute_forced():
    puzzle=[3]

    limit = 256

    while limit > 0:
        for i in range(len(puzzle)):
            if puzzle[i] == 0:
                puzzle[i] = 6
                puzzle.append(8)
                continue
            puzzle[i] -= 1

        limit -= 1
        
        print(len(puzzle))

part_b_which_is_part_a_but_not_brute_forced()
