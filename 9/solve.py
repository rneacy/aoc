import collections

from pathlib import Path

with open(Path(__file__).parent.joinpath("input"), "r") as f:
    inp = f.readline()
    players = int(inp.split(" ")[0])
    l_marble = int(inp.split("worth ")[1].split(" ")[0])

marbles = collections.deque()
player_scores = {x: 0 for x in range(players)}

def partA():
    i = 0
    c_marble = 1

    marbles.append(0) # first marble

    while c_marble < l_marble:
        for player in range(players): # place marbles
            if c_marble % 23 == 0:
                player_scores[player] += c_marble
                i = ((i - 7) % len(marbles))
                player_scores[player] += marbles[i]
                del marbles[i]
                c_marble += 1
                continue

            if len(marbles) != 1:
                i = ((i + 2) % len(marbles))
            else:
                i = 1
            marbles.insert(i, c_marble)
            c_marble += 1

    print(max(player_scores.values()))

# had to rewrite- too slow, better use of deque
def partA_fast():
    for marble in range(l_marble + 1):
        if marble % 23 == 0 and marble != 0:
            marbles.rotate(7)
            player_scores[marble % players] += marble + marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(marble)

    print(max(player_scores.values()))

try:
    #partA()
    partA_fast()
except KeyboardInterrupt:
    pass