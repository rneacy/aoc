from functools import reduce

with open("input", "r") as inp:
    puzzle = inp.readlines()

CLEAR = "."
TREE  = "#"

def tree_hits(slope):
    rows  = len(puzzle)
    cols  = len(puzzle[0][:-1])

    right, down = slope

    count = 0
    y = 0
    x = 0
    while y < rows - 1:
        x += right
        y += down
        
        if puzzle[y][x % cols] == TREE:
            count += 1

        #print(f'{y} {x} {x % COLS} {puzzle[y][x % COLS]}')

    return count

def part_A():
    print(tree_hits((3, 1)))

def part_B():
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

    ans = reduce(lambda a,b: a*b, [tree_hits(slope) for slope in slopes])

    print(ans)
part_B()
