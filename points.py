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
    dp = dot_product(p1, p2)
    return math.acos(dp)

def random_point():
    x = normal()
    y = normal()
    z = normal()
    return normalize((x, y, z))

#project p2 onto p1
def project(p1, p2):
    return scale(p1, dot_product(p1, p2))

#neg around p1
def neg(p1, p2):
    x, y, z = p2
    xp, yp, zp = project(p1, p2)
    return (2 * xp - x, 2 * yp - y, 2 * zp - z)

def random_pair():
    a = random_point()
    x, y, z = random_point()
    xp, yp, zp = project(a, (x, y, z))
    b = normalize((x - xp, y - yp, z - zp))
    return (a, b)

def midpoint(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    p3 = (x1 + x2, y1 + y2, z1 + z2)
    assert(norm(p3) > 0.001)
    return normalize(p3)



    

