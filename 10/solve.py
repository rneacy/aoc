from scipy.spatial import ConvexHull

from pathlib import Path

class Star:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def go_forward(self):
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])

    def go_back(self):
        self.pos = (self.pos[0] - self.vel[0], self.pos[1] - self.vel[1])

    def __repr__(self):
        return str((self.pos, self.vel))

stars = []

field_size_x = 200 # this works for my vs code terminal anyway
field_size_y = 10

with open(Path(__file__).parent.joinpath("input"), "r") as f:
    inp = f.read().splitlines()
    for line in inp:
        a = line.split("> ")

        posx, posy = a[0][10:].split(", ")
        velx, vely = a[1][10:-1].split(", ")

        stars.append(Star((int(posx),int(posy)),(int(velx),int(vely))))

def partA():
    smallest_hull = -1
    seconds = -1
    while True:
        # seems all points belong to the message so no worries about outliers
        hull = ConvexHull([star.pos for star in stars]).area
        if smallest_hull == -1 or hull < smallest_hull:
            smallest_hull = hull
            for star in stars:
                star.go_forward()
            seconds += 1
        else:
            print("Likely text visible at second " + str(seconds), end="\n\n")
            for star in stars:
                star.go_back()

            # get top-left most star, we can normalise using this
            first_star = min([star.pos for star in stars])

            grid = [[" " for i in range(field_size_x)] for j in range(field_size_y)] 
            
            for star in stars:
                grid[star.pos[1]-first_star[1]][star.pos[0]-first_star[0]] = "*"

            for row in grid:
                for item in row:
                    print(item,end="")
                print()

            break

partA()