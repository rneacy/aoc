from pathlib import Path
import re

with open(Path(__file__).parent.joinpath("input"), "r") as inp:
    puzzle = inp.readlines()

def parse():
    bags = {line.split(' bags contain')[0]:line.split(' bags contain')[1][1:] for line in puzzle}

    for bag in bags:
        bags[bag] = bags[bag].rstrip().replace(".", "")
        bags[bag] = re.sub(" bag(s)?", "", bags[bag]).split(", ")

        bags[bag] = [(content.split(" ", 1)[1], int(content.split(" ", 1)[0])) for content in bags[bag] if content != "no other"]

    return bags

def can_hold(bags, current, target, first=True):
    if (current == target) and not first:
        return True

    if not bags[current]:
        return False

    has = []
    for contents in bags[current]:
        has.append(can_hold(bags, contents[0], target, False));

    return any(has)


def count_bags(bags, current):
    count = 0

    if not bags[current]:
        return count

    count += sum([contents[1] for contents in bags[current]])

    for bag in bags[current]:
        for num in range(bag[1]):
            count += count_bags(bags, bag[0])

    return count

def part_a():
    bags = parse()

    print(sum([can_hold(bags, bag, 'shiny gold') for bag in bags]))

def part_b():
    bags = parse()

    print(count_bags(bags, 'shiny gold'))

part_b()