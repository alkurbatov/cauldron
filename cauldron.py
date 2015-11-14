import sys
import random

pwd = "sashenka"

def main(opts_):
    table = {}

    for i in "abcdefghijklmnopqrstuvwxyz":
        table[i] = random.randint(0, 9)

    for i,j in table.iteritems():
        print "%s : %i" % (i, j)

    g = []

    for i in pwd:
        g.append(table[i])

    print g

    d = []

    base = (g[0] + g[-1]) % 10
    d.append(base)

    l = len(g) - 1
    while len(d) != len(g):
        l -= 1

        print "---"
        print "Prev. base: %i" % base
        print "Next digit %i" % g[l]

        base = (base + g[l]) % 10
        print "Result: %i" % base

        d.append(base)

    d.append("Aa$")

    print d

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
