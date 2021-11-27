from pathlib import Path
import sys
import itertools
import functools

if len(sys.argv) > 1:
    p = sys.argv[1]
else:
    p = "input"

with open(Path(__file__).parent.joinpath(p), "r") as inp:
    puzzle = inp.readlines()
    
    fields_sep = list(itertools.takewhile(lambda line: line != "\n", puzzle))
    fields = {}
    for field in fields_sep:
        name, ranges = field.split(":")
        ranges = ranges.rstrip()[1:]
        lo_range, hi_range = ranges.split(" or ")
        lo_range = [int(n) for n in lo_range.split("-")]
        hi_range = [int(n) for n in hi_range.split("-")]
        fields[name] = (lo_range, hi_range)

    puzzle = puzzle[len(fields) + 2:]
    my_tx = [int(val) for val in puzzle[0].rstrip().split(',')]

    puzzle = puzzle[3:]
    nb_tx = [[int(val) for val in tx.rstrip().split(',')] for tx in puzzle]

def check_field_valid(field):
    if field == 0:
        return 1

    valid = False
    for check in fields:
        if (fields[check][0][0] <= field <= fields[check][0][1]) or (fields[check][1][0] <= field <= fields[check][1][1]):

            valid=True
            break

    return 0 if valid else field

def check_field_valid_with_rule(field, rule_name):
    return (fields[rule_name][0][0] <= field <= fields[rule_name][0][1]) or (fields[rule_name][1][0] <= field <= fields[rule_name][1][1])

def invalid_sum():
    error_rate = sum([check_field_valid(fld) for tx in nb_tx for fld in tx])
    print(error_rate)

def determine_fields():
    v_tx = [valid for valid in filter(lambda tx: not any([check_field_valid(fld) for fld in tx]), nb_tx)]

    cols = [ [tx[x] for tx in v_tx] for x in range(len(v_tx[0])) ]

    #print(cols)

    order = {i:None for i in range(len(cols))}
    left = list(set(fields) - set(order.values()))
    solved_for = []

    # row class seat
    while len(left) > 0:
        #print("\n\nrestart\n\n")
        #for col in cols:
        for x in range(len(cols)):
            if x in solved_for:
                continue

            if len(left) == 1:
                order[x] = left[0]
                break

            #print(f'col = {cols[x]}')
            res = {test : all([check_field_valid_with_rule(field, test) for field in cols[x]]) for test in left}
            #print(res)
            
            # Inevitably there will be a column where this is not ambigious otherwise the solve is impossible
            # Park this column for now if it satisfies more than one.
            park = list(res.values()).count(True) > 1
            if not park:
                found = list(filter(lambda x: res[x], res))[0]
                order[x] = found
                solved_for.append(x)
                #print(f"Found... {cols} , Order = {order}")
                break
            # else:
            #     print("Parking")

        left = list(set(fields) - set(order.values()))

    return order

def departure_vals():
    order = determine_fields()
    res = functools.reduce(lambda a, b: a * b, [my_tx[i] for i in order if "departure" in order[i]])

    print(order)
    print(res)

#invalid_sum()
departure_vals()