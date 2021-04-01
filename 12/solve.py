from pathlib import Path
import math

with open(Path(__file__).parent.joinpath("input"), "r") as inp:
    puzzle = inp.readlines()
    puzzle = [l.rstrip() for l in puzzle]

    directions = [(l[0], int(l[1:])) for l in puzzle]

NORTH = "N"
SOUTH = "S"
WEST  = "W"
EAST  = "E"
LEFT  = "L"
RIGHT = "R"
FORW  = "F"

def part_a():
    x = 0
    y = 0
    d = 90

    D_NORTH = 0
    D_EAST  = 90
    D_SOUTH = 180
    D_WEST  = 270

    for direction in directions:
        if direction[0] == NORTH:
            y += direction[1]
        
        if direction[0] == SOUTH:
            y -= direction[1]

        if direction[0] == WEST:
            x -= direction[1]

        if direction[0] == EAST:
            x += direction[1]

        if direction[0] == LEFT:
            d -= direction[1]
            d %= 360

        if direction[0] == RIGHT:
            d += direction[1]
            d %= 360

        if direction[0] == FORW:
            if d == D_NORTH: y += direction[1]
            if d == D_SOUTH: y -= direction[1]

            if d == D_WEST: x -= direction[1]
            if d == D_EAST: x += direction[1]

    return abs(x) + abs(y)

def part_b():
    waypoint = {"x":10, "y":1}
    ship = {"x":0, "y":0}

    for direction in directions:
        if direction[0] == FORW:
            ship['x'] += direction[1] * waypoint['x']
            ship['y'] += direction[1] * waypoint['y']

        if direction[0] == NORTH:
            waypoint['y'] += direction[1]

        if direction[0] == SOUTH:
            waypoint['y'] -= direction[1]

        if direction[0] == WEST:
            waypoint['x'] -= direction[1]

        if direction[0] == EAST:
            waypoint['x'] += direction[1]

        if direction[0] == LEFT:
            for _ in range(math.floor(direction[1] / 90)):
                old = (waypoint['x'], waypoint['y'])
                waypoint['x'] = -old[1]
                waypoint['y'] = old[0]

        if direction[0] == RIGHT:
            for _ in range(math.floor(direction[1] / 90)):
                old = (waypoint['x'], waypoint['y'])
                waypoint['x'] = old[1]
                waypoint['y'] = -old[0]

    return abs(ship['x']) + abs(ship['y'])

print(part_b())