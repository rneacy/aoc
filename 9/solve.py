from pathlib import Path

with open(Path(__file__).parent.joinpath("input"), "r") as inp:
    puzzle = inp.readlines()
    puzzle = [int(line) for line in puzzle]

PREAMBLE_LEN = 25

def find_exploit():
    for c in range(PREAMBLE_LEN, len(puzzle)):
        ok = any([(puzzle[a]+puzzle[b]==puzzle[c]) for a in range(c - PREAMBLE_LEN, c) for b in range(c - PREAMBLE_LEN, c)])

        if not ok:
            return c, puzzle[c]

    return c, -1

def part_a():
    _, num = find_exploit()
    print(num)

def part_b():
    index, target = find_exploit()
    print(f"Target is {target}.")

    s_puzzle = puzzle[:index]

    search_range = 1
    res = 0

    while res != target:
        search_range += 1

        if search_range == PREAMBLE_LEN:
            print("Something has gone wrong.")
            break

        for i in range(0, len(s_puzzle) - (search_range + 1)):
            res = sum([s_puzzle[num] for num in range(i, i + search_range)])

            if res == target:
                selection = [s_puzzle[num] for num in range(i, i + search_range)]
                print(f"{min(selection) + max(selection)}")
                break

part_b()