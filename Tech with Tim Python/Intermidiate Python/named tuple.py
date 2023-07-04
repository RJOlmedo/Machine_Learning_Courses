from collections import namedtuple

Point = namedtuple("Point", "x y z")

newP = Point(3,4,5)
print(newP.x, newP.y, newP.z)
print(newP[0])