#!/usr/bin/env python

# This file is a part of Squirrel project
#
# Copyright (C) 2015, Alexander Kurbatov <sir.alkurbatov@yandex.ru>
#
# Cauldron is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Cauldron is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import random
import optparse

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
    parser = optparse.OptionParser("%prog", version="%prog 0.01")
    parser.add_option("-p", action = "store", type = "string", dest="pepper",
        help = "text addition used to bypass some strict password requirements")

    (opts, args) = parser.parse_args()

    m = Map()
    p = Permutation()

    print "Map: " + os.linesep + str(m) + \
          os.linesep + \
          "Permutation: " + os.linesep + str(p)

    g = m.encode("sashenka")
    print g

    d = []
    if opts.pepper:
        d.append(opts.pepper)

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

