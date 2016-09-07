from points import *
from heat_kernel import *
import numpy

size = 5

def random_angle():
    return numpy.random.uniform(0.0, 2 * math.pi)

def great_circle_point(angle, basis):
    ((x1, y1, z1), (x2, y2, z2)) = basis
    a = math.cos(angle)
    b = math.sin(angle)
    return (a * x1 + b * x2, a * y1 + b * y2, a * z1 + b * z2)    

def test_0(points, time):
    origin = (1, 0, 0)
    m = numpy.zeros(shape=(size, size))
    for i in range(size):
        for j in range(i + 1):
            p1 = points[i]
            if i == j:
                matrix_entry = heat_kernel_2(origin, p1, time)*heat_kernel_1(0.0, time)
            else:                
                p2 = points[j]
                mid = midpoint(p1, p2)
                matrix_entry = heat_kernel_2(origin, mid, time)*heat_kernel_2(mid, p1, time)
            
            m[i, j] = matrix_entry
            m[j, i] = matrix_entry
    try:
        numpy.linalg.cholesky(m)
        print "Success"
        print m
    except numpy.linalg.LinAlgError:
        print "Failed"
        w, v = numpy.linalg.eig(m)
        print w
        print m

def test_1():
    points = [random_point() for i in range(size)]
    test_0(points, 0.3)

def test_2():
    angles = [random_angle() for i in range(size)]
    basis = random_pair()
    points = [great_circle_point(angle, basis) for angle in angles]
    test_0(points, 0.3)
