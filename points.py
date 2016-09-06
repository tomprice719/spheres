import math
from numpy.random import normal

def dot_product(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return x1 * x2 + y1 * y2 + z1 * z2

def norm(p):
    return math.sqrt(dot_product(p, p))

def scale(v, s):
    x, y, z = v
    return x * s, y * s, z * s

def normalize(v):
    return scale(v, 1/norm(v))

def angle(p1, p2):
    p1=normalize(p1)
    p2=normalize(p2)
    return math.acos(dot_product(p1, p2))

def random_point():
    x = normal()
    y = normal()
    z = normal()
    return normalize((x, y, z))

def project(p1, p2):
    return scale(p2, dot_product(p1, p2))

def neg(p1, p2):
    x, y, z = p1
    xp, yp, zp = project(p1, p2)
    return (2 * xp - x, 2 * yp - y, 2 * zp - z)


