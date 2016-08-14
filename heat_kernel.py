from scipy.special import sph_harm
import numpy as np

max_degree = 50
evaluations = {}

#Eigenvalue is -degree(degree - 1) / r^2

def compute_evaluations(angle):
    for degree in range(max_degree):
        acc = 0.0
        for order in range(-degree, degree + 1):
            origin_value = sph_harm(order, degree, 0.0, 0.0)
            acc += np.real(sph_harm(order, degree, 0.0, angle) * np.conj(origin_value))
        yield acc    

def get_evaluations(angle):
    if angle in evaluations:
        return evaluations[angle]
    e = list(compute_evaluations(angle))
    evaluations[angle] = e
    return e

def heat_kernel(angle, time):
    e = get_evaluations(angle)
    acc = 0.0
    for degree in range(max_degree):
        acc += np.exp(-degree * (degree + 1) * time) * e[degree]
    return acc





