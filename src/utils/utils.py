import numpy as np
from collections.abc import Iterable

def create_point(xyz):
    return np.append(np.array(xyz),1)

def create_vector(xyz):
    return np.append(np.array(xyz),0)

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
    
def add_tuples(a, b):
    return a + b

def substract_tuples(a, b):
    return a - b