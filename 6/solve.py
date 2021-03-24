from scipy import spatial as sp
import numpy as np

from pathlib import Path

with open(Path(__file__).parent.joinpath("input"), "r") as f:
    inp = f.read().splitlines()

_manhattan = 1

points = []

# split points
x_left_edge = -1
x_right_edge = -1
y_top_edge = -1
y_bottom_edge = -1

for line in inp:
    sep = line.split(",")
    x = int(sep[0])
    y = int(sep[1][1:])

    points.append([x,y])

    if x_left_edge == -1 or x < x_left_edge:
        x_left_edge = x
    if x_right_edge == -1 or x > x_right_edge:
        x_right_edge = x
    if y_top_edge == -1 or y < y_top_edge:
        y_top_edge = y
    if y_bottom_edge == -1 or y > y_bottom_edge:
        y_bottom_edge = y

tree = sp.KDTree(points)

arrayx = x_right_edge - x_left_edge
arrayy = y_bottom_edge - y_top_edge
nodes = np.zeros([arrayy, arrayx], dtype=int)

def partA():  
    for x in range(x_left_edge, x_right_edge):
        for y in range(y_top_edge, y_bottom_edge):
            dist, index = tree.query([x,y], k = 2, p = _manhattan)

            if len(set(dist)) >= 1: # exclude ambigious points
                nodes[y - y_top_edge, x - x_left_edge] = index[0]
            else:
                nodes[y - y_top_edge, x - x_left_edge] = -1

    _, counts = np.unique(nodes, return_counts=True)
    print(max(counts))


def partB():
    rsize = 0
    for x in range(x_left_edge, x_right_edge):
        for y in range(y_top_edge, y_bottom_edge):
            dist, _ = tree.query([x,y], k = len(points), p = _manhattan)

            if np.sum(dist) < 10000:
                rsize += 1

    print(rsize)

#partA()
partB()