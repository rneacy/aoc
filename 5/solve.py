from pathlib import Path
from functools import reduce
from itertools import chain
import sys

class Pipe:
    def __init__(self, x1, y1, x2, y2):
        self.start = {'x':int(x1), 'y':int(y1)}
        self.end = {'x':int(x2), 'y':int(y2)}

    def __str__(self):
        return f's:{self.start}, e:{self.end}'

    def __repr__(self):
        return f"Pipe: [{self.__str__()}]"

if len(sys.argv) > 1:
    p = sys.argv[1]
else:
    p = "input"

with open(Path(__file__).parent.joinpath(p), "r") as inp:
    puzzle = [l.rstrip() for l in inp.readlines()]
    pipes = []
    for pipe in puzzle:
        spl = pipe.split(" -> ")
        x1, y1 = spl[0].split(",")
        x2, y2 = spl[1].split(",")
        pipes.append(Pipe(x1, y1, x2, y2))

    max_x = reduce(lambda big, x: x if x > big else big, [max(pipe.start['x'], pipe.end['x']) for pipe in pipes]) + 1
    max_y = reduce(lambda big, y: y if y > big else big, [max(pipe.start['y'], pipe.end['y']) for pipe in pipes]) + 1
    field = [[0 for _ in range(max_x)] for _ in range(max_y)]


def part_a():
    f_pipes = list(filter(lambda pipe: (pipe.start['x'] == pipe.end['x']) or (pipe.start['y'] == pipe.end['y']), pipes))
    
    for pipe in f_pipes:
        if pipe.start['x'] == pipe.end['x']:
            for y in range(min(pipe.start['y'], pipe.end['y']), max(pipe.start['y'], pipe.end['y']) + 1):
                field[y][pipe.start['x']] += 1
        else:
            for x in range(min(pipe.start['x'], pipe.end['x']), max(pipe.start['x'], pipe.end['x']) + 1):
                field[pipe.start['y']][x] += 1

    overlaps = reduce(lambda count, n: count+1 if n > 1 else count, list(chain(*field)))
    print(overlaps)

def part_b():
    for pipe in pipes:
        t_field = [[0 for _ in range(max_x)] for _ in range(max_y)]
        # Straight vertical
        if pipe.start['x'] == pipe.end['x']:
            for y in range(min(pipe.start['y'], pipe.end['y']), max(pipe.start['y'], pipe.end['y']) + 1):
                field[y][pipe.start['x']] += 1
                t_field[y][pipe.start['x']] += 1
        # Straight horizontal
        elif pipe.start['y'] == pipe.end['y']:
            for x in range(min(pipe.start['x'], pipe.end['x']), max(pipe.start['x'], pipe.end['x']) + 1):
                field[pipe.start['y']][x] += 1
                t_field[pipe.start['y']][x] += 1
        # Right-facing diagonal
        elif pipe.start['x'] < pipe.end['x']:
            x = pipe.start['x']
            for y in range(min(pipe.start['y'], pipe.end['y']), max(pipe.start['y'], pipe.end['y']) + 1):
                field[y][x] += 1
                t_field[y][x] += 1
                x += 1
        # Left-facing diagonal
        elif pipe.start['x'] > pipe.end['x']:
            if pipe.start['y'] < pipe.end['y']:
                x = pipe.start['x']
                for y in range(min(pipe.start['y'], pipe.end['y']), max(pipe.start['y'], pipe.end['y']) + 1):
                    field[y][x] += 1
                    t_field[y][x] += 1
                    x -= 1
            else:
                x = pipe.end['x']
                for y in range(min(pipe.start['y'], pipe.end['y']), max(pipe.start['y'], pipe.end['y']) + 1):
                    field[y][x] += 1
                    t_field[y][x] += 1
                    x += 1
        print(pipe)
        for line in t_field:
            print("".join([str(ok) if ok != 0 else '.' for ok in line]))
        print("")

        print("")
        for line in field:
            print("".join([str(ok) if ok != 0 else '.' for ok in line]))
        print("")

    overlaps = reduce(lambda count, n: count+1 if n > 1 else count, list(chain(*field)))
    print(overlaps)

part_b()