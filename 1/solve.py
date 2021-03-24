with open("input", "r") as inp:
    puzzle = inp.read()

puzzle = [int(n) for n in puzzle.split("\n") if n]

def partA():
    for i in range(len(puzzle)):
        for x in range(i, len(puzzle)):
            if puzzle[i] + puzzle[x] == 2020:
                print(puzzle[i] * puzzle[x])

def partB():
    for i in range(len(puzzle)):
        for x in range(i+1, len(puzzle)):
            for y in range(x+1, len(puzzle)):
                if puzzle[i] + puzzle[x] + puzzle[y] == 2020:
                    print(puzzle[i] * puzzle[x] * puzzle[y])

partB()
