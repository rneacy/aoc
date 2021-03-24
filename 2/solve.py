from pathlib import Path

with open(Path(__file__).parent.joinpath("input"), "r") as f:
    ids = f.read().splitlines() # no \n

def partA():
    twos = 0
    threes = 0
    for box in ids:
        has_two, has_three = parse_box_id(box)

        if has_two:
            twos += 1
        if has_three:
            threes += 1

    res = twos * threes
    print(res)

def partB():
    for box in ids:
        # verify against each other box id
        for other_box in ids:
            if box == other_box:
                continue

            diff_index = -1
            bad_box = False

            for i in range(len(box)):
                if box[i] != other_box[i]:
                    if diff_index == -1: # this is the first difference
                        diff_index = i
                    else: # there has been a diff elsewhere, box is useless
                        bad_box = True

            if not bad_box:
                print(box[:diff_index] + box[diff_index + 1:])
                return

def parse_box_id(box_id: str):
    letters = {}
    for letter in box_id:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    has_two = False
    has_three = False

    for count in letters.values():
        if count == 2:
            has_two = True
        if count == 3:
            has_three = True

    return has_two, has_three

#partA()
partB()