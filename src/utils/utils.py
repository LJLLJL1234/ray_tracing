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

def negate_tuple(a):
    return -a

def multiply_tuple(a, b):
    return a * b

def divide_tuple(a, b):
    return a / b

def magnitude(vector):
    return np.linalg.norm(vector)

def normalize(vector):
    return vector / magnitude(vector)

def dot_product(a, b):
    return np.dot(a, b)

def cross_product(a, b):
    a_values = a[:-1]
    b_values = b[:-1]
    return np.cross(a_values, b_values)

def round_to_int(vector):
    return np.round(vector).astype(int)