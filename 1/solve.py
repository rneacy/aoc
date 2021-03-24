from pathlib import Path

with open(Path(__file__).parent.joinpath("input"), "r") as f:
    insts = f.readlines()

add = "+"
minus = "-"

def partA():
    freq = 0
    for i in range(0, len(insts)):
        operator = insts[i][:1]
        number = int(insts[i][1:-1])
        
        if operator == add:
            freq += number
        else:
            freq -= number

    print(freq)

def partB():
    freq = 0
    reached_freqs = set()
    cond = False
    
    while not cond:
        for i in range(0, len(insts)):
            operator = insts[i][:1]
            number = int(insts[i][1:-1])
            
            if operator == add:
                freq += number
            else:
                freq -= number

            if freq in reached_freqs:
                cond = True
                break
            else:
                reached_freqs.add(freq)

    print(freq)

#partA()
partB()