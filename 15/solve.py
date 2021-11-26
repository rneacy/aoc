from pathlib import Path
import sys

if len(sys.argv) > 1:
    p = sys.argv[1]
else:
    p = "input"

with open(Path(__file__).parent.joinpath(p), "r") as inp:
    puzzle = inp.readline()
    puzzle = [int(v.rstrip()) for v in puzzle.split(',')]

def solve(stop):
    track = {puzzle[i-1] : i for i in range(1, len(puzzle))}  # Init the first rounds, but leave last out as we need to 'buffer' this to know if new
    last = puzzle[-1:][0]

    for r in range(len(puzzle)+1, stop+1):  # rounds are indexed from 1
        if last in track:
            new = (r - 1) - track[last]
        else:
            new = 0
            
        track[last] = r - 1
        last = new

    print(last)

#solve(2020)
solve(30000000)