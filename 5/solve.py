from pathlib import Path

with open(Path(__file__).parent.joinpath("input"), "r") as f:
    inp = f.readline()
    inp = list(inp)
    if inp[-1] == "\n":
        del inp[-1]

def react(alleles: list) -> int:
    i = 0
    while True: # the array changes size so using for/range is iffy
        if (i + 1) >= len(alleles):
            break # avoid overflow

        delete = False

        if alleles[i].isupper():
            if alleles[i+1].islower():
                if alleles[i].lower() == alleles[i+1]:
                    delete = True
        else:
            if alleles[i+1].isupper():
                if alleles[i].upper() == alleles[i+1]:
                    delete = True

        if delete:
            del alleles[i]
            del alleles[i] # for some reason slices don't work here
            i = i - 1
        else:
            i = i + 1

    return len(alleles)

def partB():
    print("Running...")

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    al_copy = inp.copy()
    original = al_copy.copy()
    smallest = -1

    for letter in alpha:
        i = 0
        while True:
            if al_copy[i] == letter or al_copy[i].upper() == letter:
                del al_copy[i]
                i -= 1
            else:
                i += 1
            
            if i >= len(al_copy):
                # react it
                length = react(al_copy)
                if smallest == -1 or length < smallest:
                    smallest = length

                al_copy = original.copy()
                break

    print("Smallest polymer length: " + str(smallest))

#react(inp) # part a
partB()