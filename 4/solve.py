from pathlib import Path
import sys

if len(sys.argv) > 1:
    p = sys.argv[1]
else:
    p = "input"

with open(Path(__file__).parent.joinpath(p), "r") as inp:
    puzzle = [l.rstrip() for l in inp.readlines()]

    calls = puzzle[0].split(",")
    calls = [call for call in calls]
    boards = [[]]

    line = 2
    board = 0
    while line < len(puzzle):
        if(puzzle[line] != ''):
            boards[board] += [num for num in puzzle[line].split()]
        else:
            boards.append([])
            board += 1

        line+=1

MARK = "X"
WIN = [MARK for _ in range(5)]

def get_row(board, i):
    r = i*5
    return board[r:r+5]

def get_col(board, i):
    return board[i::5]

def get_diag(board, dir):
    if dir=="r":
        return board[::6]
    else:
        return board[4:4*5+1:4]

def unmarked(board):
    return [x for x in board if x.isdigit()]

def part_a():
    for call in range(len(calls)):
        for board in boards:
            try:
                i = board.index(calls[call])
                board[i] = MARK
            except ValueError:
                continue

            if any([get_row(board, i) == WIN for board in boards for i in range(5)]) or\
                    any([get_col(board, i) == WIN for board in boards for i in range(5)]):
                ans = sum([int(x) for x in unmarked(board)]) * int(calls[call])
                print(ans)
                return

def part_b():
    still_playing = boards.copy()
    for call in range(len(calls)):
        for board in boards:
            try:
                i = board.index(calls[call])
                board[i] = MARK
            except ValueError:
                continue

            if any([get_row(board, i) == WIN for board in boards for i in range(5)]) or\
                    any([get_col(board, i) == WIN for board in boards for i in range(5)]):
                ans = sum([int(x) for x in unmarked(board)]) * int(calls[call])
                print(ans)
                return

part_a()