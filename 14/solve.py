from pathlib import Path
import numpy as np
import re
import math

BIT_LEN = 36

with open(Path(__file__).parent.joinpath("input"), "r") as inp:
    puzzle = inp.readlines()
    puzzle = [l.rstrip() for l in puzzle]

    programs = []
    prog_index = -1

    for line in range(len(puzzle)):
        if "mask" in puzzle[line]:
            programs.append({})
            prog_index += 1
                
            programs[prog_index]['mask'] = list(puzzle[line].split("mask = ")[1])
            programs[prog_index]['insts'] = []
        else:
            addr = int(re.findall("\[[0-9]+\]", puzzle[line])[0][1:-1])
            val = int(re.findall(" [0-9]+", puzzle[line])[0][1:])

            val = list(bin(val)[2:])
            val = list("0" * (BIT_LEN - len(val))) + val

            programs[prog_index]['insts'].append({"addr": addr, "val": val})

def b_to_i(byte):
    return int(''.join(byte), 2)

def bin_permute(n):
    perms = []
    for i in range(int(math.pow(2, n))):
        to_add = bin(i)[2:]
        
        perms.append('0' * (n - len(to_add)) + to_add)

    return perms

def part_a():
    memory = {}

    for program in programs:
        for inst in program["insts"]:

            write_val = []

            for i in range(BIT_LEN):
                mask_chr = program['mask'][BIT_LEN - i - 1]

                if mask_chr == "X":
                    write_val.append(inst['val'][BIT_LEN - i - 1])
                    continue

                write_val.append(mask_chr)

            memory[inst['addr']] = write_val[::-1]

    return sum([b_to_i(memory[addr]) for addr in memory])

def part_b():
    memory = {}

    for program in programs:
        floatingIndices = [i for i in range(len(program['mask'])) if program['mask'][i] == "X"]
        permutations = bin_permute(len(floatingIndices))

        for inst in program["insts"]:
            addr = list(bin(inst['addr'])[2:])
            addr = list("0" * (BIT_LEN - len(addr))) + addr

            new_addr = []

            for i in range(BIT_LEN):
                mask_chr = program['mask'][BIT_LEN - i - 1]

                if mask_chr == "X":
                    new_addr.append('0')
                    continue

                if mask_chr == "0":
                    new_addr.append(addr[BIT_LEN - i - 1])
                    continue

                new_addr.append('1')

            new_addr = new_addr[::-1]

            for perm in permutations:
                for i in range(len(perm)):
                    new_addr[floatingIndices[i]] = perm[i]

                memory[b_to_i(new_addr)] = inst['val']

    return sum([b_to_i(memory[addr]) for addr in memory])

print(part_b())