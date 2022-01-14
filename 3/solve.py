from pathlib import Path
import sys

if len(sys.argv) > 1:
    p = sys.argv[1]
else:
    p = "input"

with open(Path(__file__).parent.joinpath(p), "r") as inp:
    puzzle = [l.rstrip() for l in inp.readlines()]

def invert(binary):
    return "".join(['0' if num == '1' else '1' for num in list(binary)])

def part_a():
    cols = len(puzzle[0])
    rows = len(puzzle)
    gamma = ''

    for x in range(cols):
        zeroes = len([int(puzzle[y][x]) for y in range(rows) if puzzle[y][x] == '0'])
        gamma += '0' if zeroes >= (rows/2) else '1'

    epsilon = invert(gamma)

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print(gamma * epsilon)

def part_b():
    def whittle_down(keep='1'):
        p_copy = puzzle.copy()

        col_check = 0
        while len(p_copy) != 1:
            _keep = keep
            zeroes = len([int(p_copy[y][col_check]) for y in range(len(p_copy)) if p_copy[y][col_check] == '0'])
            if zeroes>len(p_copy)/2:
                _keep = '0' if keep == '1' else '1'
            p_copy = list(filter(lambda num: list(num)[col_check] == _keep, p_copy))
            col_check += 1

        return p_copy[0]

    o2  = int(whittle_down(), 2)
    co2 = int(whittle_down('0'), 2)

    print(o2 * co2)

part_b()