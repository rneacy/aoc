from pathlib import Path

with open(Path(__file__).parent.joinpath("input"), "r") as inp:
    puzzle = inp.readlines()

def parse():
    groups = []

    c_group = []
    for line in puzzle:
        if line == "\n":
            groups.append(c_group)
            c_group = []
            continue

        line = line.rstrip()
        
        answers = list(line)
        c_group.append(answers)

    groups.append(c_group)
    return groups

def part_A():
    groups = parse()
    total = 0
    for group in groups:
        uniques = set()
        for person in group:
            uniques.update(person)
        
        total+=len(uniques)

    print(total)

def part_B():
    groups = parse()
    total = 0
    for group in groups:
        counts = {}
        for person in group:
            for ans in person:
                if counts.get(ans) is None:
                    counts[ans] = 1
                else:
                    counts[ans] += 1

        agreed = [question for question in counts if counts[question] == len(group)]

        total += len(agreed)
        
    print(total)

part_B()