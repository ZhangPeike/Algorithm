#!/usr/bin/python
import math


def main():
    p1 = Point(0, 0, 0)
    p2 = Point(0, 0, 0)
    print Point.distance(p1, p2)
    print "Hello world"


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def distance(p1, p2):
        error = (p1.x-p2.x) ^ 2 + (p1.y-p2.y) ^ 2 + (p1.z-p2.z) ^ 2
        print error
        return math.sqrt(error)


if __name__ == "__main__":
    main()
