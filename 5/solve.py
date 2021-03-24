from pathlib import Path
import math
import pandas as pd

with open(Path(__file__).parent.joinpath("input"), "r") as inp:
    puzzle = inp.readlines()
    puzzle = [line.rstrip() for line in puzzle]

ROWS = 128
COLS = 8

FRONT = "F"
BACK  = "B"
LEFT  = "L"
RIGHT = "R"

def _partition(index, seat, lower, upper):
    if abs(lower - upper) == 1:
        if seat[index] == FRONT or seat[index] == LEFT:
            return lower
        else:
            return upper

    if seat[index] == FRONT or seat[index] == LEFT:
        upper -= math.ceil((upper-lower)/2)
    else:
        lower += math.ceil((upper-lower)/2)

    index += 1
    return _partition(index, seat, lower, upper)

def find_seat(seat):
    seat_row = _partition(0, seat[:7], 0, ROWS-1)
    seat_col = _partition(0, seat[-3:], 0, COLS-1)

    return (seat_row, seat_col), (seat_row * 8) + seat_col

def part_a():
    seat_ids = []
    for seat in puzzle:
        _, id = find_seat(seat)
        seat_ids.append(id)

    print(max(seat_ids))

def part_b():
    full_col = [x for x in range(8)]
    seats = []
    for seat in puzzle:
        new_seat, _ = find_seat(seat)
        seats.append(new_seat)

    rows = {seat[0]:[inner_seat[1] for inner_seat in seats if seat[0] == inner_seat[0]] for seat in seats}

    for row in rows:
        missing = [r for r in full_col if r not in rows[row]]

        if missing:
            print(f"Seat {row}/{missing[0]} is vacant.")
            seat_id = row * 8 + missing[0]
            print(f"Seat ID: {seat_id}")
            break

part_b()