import numpy as np


tracks = []
carts = []

def turn_left(v):
    rot = np.array([[0, 1], [-1, 0]])
    return v.dot(rot)


def turn_right(v):
    rot = np.array([[0, -1], [1, 0]])
    return v.dot(rot)


class Cart():
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.state = 0
        return

    def move(self):
        self.pos += self.vel
        if tracks[self.pos[0]][self.pos[1]] == '+':
            if self.state == 0:
                self.state = 1
                self.vel = turn_left(self.vel)
            elif self.state == 1:
                self.state = 2
            elif self.state == 2:
                self.state = 0
                self.vel = turn_right(self.vel)

        elif tracks[self.pos[0]][self.pos[1]] == '/':
            if tuple(self.vel) == (1, 0) or tuple(self.vel) == (-1, 0):
                self.vel = turn_right(self.vel)
            else:
                self.vel = turn_left(self.vel)

        elif tracks[self.pos[0]][self.pos[1]] == '\\':
            if tuple(self.vel) == (1, 0) or tuple(self.vel) == (-1, 0):
                self.vel = turn_left(self.vel)
            else:
                self.vel = turn_right(self.vel)
        return

line = input()
line_count = 0
while line != '':
    track_list = list(line)
    if '>' in track_list:
        carts.append(Cart(np.array([line_count, track_list.index('>')]),
                          np.array([0, 1])))
    if '^' in track_list:
        carts.append(Cart(np.array([line_count, track_list.index('^')]),
                          np.array([-1, 0])))
    if '<' in track_list:
        carts.append(Cart(np.array([line_count, track_list.index('<')]),
                          np.array([0, -1])))
    if 'v' in track_list:
        carts.append(Cart(np.array([line_count, track_list.index('v')]),
                          np.array([1, 0])))
    tracks.append(track_list)
    line_count += 1
    line = input()

while True:
    carts = sorted(carts, key=lambda t: t.pos[1])
    carts = sorted(carts, key=lambda t: t.pos[0])
    for cart in carts:
        cart.move()
        a = tuple(cart.pos)
        for cart2 in carts:
            if cart2 != cart and a == tuple(cart2.pos):
                print(a)
                import sys
                sys.exit(0)
