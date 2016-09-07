from points import *
from heat_kernel import *
import numpy

size = 10

def random_angle():
    return numpy.random.uniform(0.0, 2 * math.pi)

def great_circle_point(angle, basis):
    ((x1, y1, z1), (x2, y2, z2)) = basis
    a = math.cos(angle)
    b = math.sin(angle)
    return (a * x1 + b * x2, a * y1 + b * y2, a * z1 + b * z2)
    

def test_0(angles, basis, time):
    origin = (1, 0, 0)
    m = numpy.zeros(shape=(size, size))
    for i in range(size):
        for j in range(i + 1):        
            midpoint = great_circle_point((angles[i] + angles[j]) / 2, basis)
            angle_to_midpoint = abs(angles[i] - angles[j]) / 2
            matrix_entry = heat_kernel_2(origin, midpoint, time) * heat_kernel_1(angle_to_midpoint, time)
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

def test_1():
    angles = [random_angle() for i in range(size)]
    basis = random_pair()
    time = 0.3
    test_0(angles, basis, time)
