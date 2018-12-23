import re

class Nanobot:
    def __init__(self, pos, r):
        assert isinstance(pos, list)
        assert len(pos) == 3
        assert isinstance(r, int)
        self.pos = pos
        self.r = r
        return

    def __repr__(self):
        return "{} {}".format(repr(tuple(self.pos)), self.r)

    def distance(self, b):
        return abs(self.pos[0] - b.pos[0]) +\
               abs(self.pos[1] - b.pos[1]) +\
               abs(self.pos[2] - b.pos[2])

p = re.compile('[+-]?\d+(?:\.\d+)?')

line = input()
nanobots = list()
max_bot = None
while line != '':
    parts = p.findall(line)
    bot = Nanobot([int(t) for t in parts[:-1]], int(parts[-1]))
    if max_bot is None or max_bot.r < bot.r:
        max_bot = bot
    nanobots.append(bot)
    line = input()

print(sum(1 for t in nanobots if max_bot.distance(t) <= max_bot.r))
