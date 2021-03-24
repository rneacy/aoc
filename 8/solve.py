from pathlib import Path
import copy

with open(Path(__file__).parent.joinpath("input"), "r") as inp:
    puzzle = inp.readlines()

    program = [line.split(" ") for line in puzzle]

    for i in range(len(program)):
        program[i][1] = int(program[i][1].rstrip())

#* INSTRUCTION CONSTANTS
CMD  = 0
VAL  = 1

CMDS = ['acc', 'jmp', 'nop']

def compute(program):
    ACC  = 0
    PC   = 0

    pc_cache = []

    while PC < len(program):
        if PC in pc_cache:
            return False, ACC

        if program[PC][CMD] == 'acc':
            ACC += program[PC][VAL]
        
        elif program[PC][CMD] == 'jmp':
            pc_cache.append(PC)
            PC += program[PC][VAL]
            continue

        pc_cache.append(PC)
        PC+=1

    return True, ACC

def part_a():
    print(compute(program)[1])

def part_b():
    terminates = False

    i = 0
    last_acc = 0
    while not terminates:
        this_program = copy.deepcopy(program)
        
        if this_program[i][CMD] == "nop":
            this_program[i][CMD] = "jmp"

        elif this_program[i][CMD] == "jmp":
            this_program[i][CMD]  = "nop"

        else:
            i+=1
            continue

        terminates, last_acc = compute(this_program)
        i+=1

    print(last_acc)

part_b()