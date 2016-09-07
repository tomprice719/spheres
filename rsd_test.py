from points import *
from heat_kernel import *

def test_rsd_1(p1, p2, time):
    origin = (1, 0, 0)
    p3 = neg(p1, p2)
    LS = (heat_kernel_2(origin, p1, time) * heat_kernel_2(p1, p2, time))**2
    RS = (heat_kernel_2(origin, origin, time))**2 * heat_kernel_2(origin, p2, time) * heat_kernel_2(origin, p3, time)
    print LS, RS
    if(LS > RS and 1/RS > 1/LS):
        print "FAILED", LS, RS
        print p1
        print p2

def test_rsd_2():
    p1 = random_point()
    p2 = random_point()
    for time in range(5, 150):
        test_rsd_1(p1, p2, time / 30.0)

def test_rsd_3():
    for i in range(50):
        test_rsd_2()
        print "FINISHED", i
