import re
from pathlib import Path

with open(Path(__file__).parent.joinpath("input"), "r") as inp:
    puzzle = inp.readlines()

# cid is allowed
required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

v_byr = range(1920, 2002+1)
v_iyr = range(2010, 2020+1)
v_eyr = range(2020, 2030+1)
v_hgy_cm = range(150, 193+1)
v_hgy_in = range(59, 76+1)
v_hcl = "#([0-9a-f]){6}"
v_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
v_pid = 9

def parse(puzzle):
    passports = []

    c_passport = {}
    for line in puzzle:
        if line == "\n":
            passports.append(c_passport)
            c_passport = {}
            continue

        entries = line.split(" ")
        
        for entry in entries:
            key, val = entry.split(":")
            c_passport[key] = val.rstrip()

    passports.append(c_passport)

    return passports

def part_A():
    passports = parse(puzzle)
    # check keys
    valid = []
    for passport in passports:
        if all(item in list(passport.keys()) for item in required):
            valid.append(passport)

    print(len(valid))
    return valid

def part_B():
    present = part_A()

    valid = 0
    count = -1

    for passport in present:
        count += 1
        # birth year
        if not (int(passport['byr']) in v_byr and
            int(passport['iyr']) in v_iyr and
            int(passport['eyr']) in v_eyr):
            continue

        hgt_type = passport['hgt'][-2:]
        if not any(measure in hgt_type for measure in ["cm", "in"]):
            continue
        if hgt_type == "cm":
            if not int(passport['hgt'][:-2]) in v_hgy_cm:
                continue
        elif not int(passport['hgt'][:-2]) in v_hgy_in:
            continue
        if not (re.search(v_hcl, passport['hcl']) and
            any(item in passport['ecl'] for item in v_ecl) and
            len(passport['pid']) == v_pid):
            continue

        valid += 1

    print(f"Valid passports: {valid}")

part_B()
