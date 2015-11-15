import os
import sys
import random

class Permutation(object):
    def __init__(self):
        self.data = random.sample(xrange(10), 10)

    def apply(self, val_):
        x = val_ % len(self.data)

        return self.data[(self.data.index(x) + 1) % len(self.data)]

    def __str__(self):
        return str(self.data)

class Map(object):
    def __init__(self):
        self.data = {}
        for i in "abcdefghijklmnopqrstuvwxyz":
            self.data[i] = random.randint(0, 9)

    def encode(self, src_):
        return [self.data[i] for i in src_]

    def __str__(self):
        return str(self.data)

def main(opts_):
    m = Map()
    p = Permutation()

    print "Map: " + os.linesep + str(m) + \
          os.linesep + \
          "Permutation: " + os.linesep + str(p)

    g = m.encode("sashenka")
    print g

    d = ["Aa$"]

    base = g[0]
    for i in reversed(g):
        print "---"
        print "Prev. base: %i" % base
        print "Next digit %i" % i

        base = p.apply(base + i)
        print "Result: %i" % base

        d.append(base)

    print d

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

