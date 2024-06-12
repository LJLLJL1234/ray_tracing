import numpy as np
from collections.abc import Iterable

def create_point(x, y, z):
    return np.array([x, y ,z, 1])

def create_vector(x, y, z):
    return np.array([x, y, z, 0])

def _is_point(vector):
    return vector[3] == 1

def _is_vector(vector):
    return vector[3] == 0

def _is_close(a, b, tol=1e-5): 
    if isinstance(a, Iterable) and isinstance(b, Iterable):
        if a.shape != b.shape:
            return False
        else:
            return np.abs(a - b).all() < tol
    else:
        return np.abs(a - b) < tol