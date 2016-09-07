from scipy.special import sph_harm
from points import angle
import numpy as np
import math

projective = True

max_degree = 50
projections = {}

#Eigenvalue is -degree(degree + 1) / r^2

def compute_projections(angle):
    for degree in range(max_degree):
        acc = 0.0
        for order in range(-degree, degree + 1):
            origin_value = sph_harm(order, degree, 0.0, 0.0)
            acc += np.real(sph_harm(order, degree, 0.0, angle) * np.conj(origin_value))
        yield acc    

def get_projections(angle):
    if angle in projections:
        return projections[angle]
    e = list(compute_projections(angle))
    projections[angle] = e
    return e

def heat_kernel_0(angle, time):
    e = get_projections(angle)
    acc = 0.0
    for degree in range(max_degree):
        acc += np.exp(-degree * (degree + 1) * time) * e[degree]
    return acc * 4 * math.pi

def heat_kernel_1(angle, time):
    if projective:
        return (heat_kernel_0(angle, time) + heat_kernel_0(math.pi - angle, time)) / 2
    return heat_kernel_0(angle, time)

def heat_kernel_2(p1, p2, time):
    a = angle(p1, p2)
    return heat_kernel_1(a, time)





