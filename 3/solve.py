import numpy as np

from pathlib import Path

with open(Path(__file__).parent.joinpath("input"), "r") as f:
    claims = f.read().splitlines()

grid = np.zeros((1050, 1050), dtype=int)
valid_ids = {}

print_grid = False

def partA(): # includes part b
    init_ids()

    for claim in claims:
        c,x,y,w,h = parse_claim(claim)

        cY = y
        cX = x

        for _ in range(w):
            for _ in range(h):
                if grid[cY, cX] == 0:
                    grid[cY, cX] = c
                else:
                    # exclude both claims from valid ids
                    valid_ids[grid[cY, cX] - 1] = False
                    valid_ids[c - 1] = False

                    grid[cY, cX] = -1
                
                cY += 1
            cX +=1
            cY = y

    # count the overlaps
    sqm = 0
    for row in grid:
        for a in row:
            if a == -1:
                sqm += 1

    print("Overlap sqM: " + str(sqm))
    if print_grid:
        print(grid)

    for claim in valid_ids:
        if valid_ids[claim] == True:
            print("Whole claim: " + str(claim + 1))


def parse_claim(claim: str):
    claim = claim.split("@ ")
    
    pos_data, size_data = claim[1].split(": ")
    pos_data = pos_data.split(",")
    size_data = size_data.split("x")

    x = int(pos_data[0])
    y = int(pos_data[1])

    w = int(size_data[0])
    h = int(size_data[1])

    c = int(claim[0][1:-1])

    return c,x,y,w,h

def init_ids():
    for i in range(len(claims)):
        valid_ids[i] = True

partA()