import pytest
import numpy as np
# import sys
# sys.path.append('/Users/Lauri.Lehtola/private_projects/ray_tracing')
from src.utils.utils import _is_point, create_point, _is_vector, create_vector, _is_close, add_tuples, substract_tuples, negate_tuple, multiply_tuple, divide_tuple, magnitude, normalize, dot_product

@pytest.mark.parametrize(
    "coordinates, expected",
    [
        (np.array([1, 2, 3, 1]), True),
        (np.array([1, 2, 3, 0]), False),
    ],
)
def test_is_point(coordinates, expected):
    assert _is_point(coordinates) == expected

def test_create_point():
    assert np.array_equal(create_point((1, 2, 3)), np.array([1, 2, 3, 1]))
                          
@pytest.mark.parametrize(
    "coordinates, expected",
    [
        (np.array([1, 2, 3, 0]), True),
        (np.array([1, 2, 3, 1]), False),
    ],
)
def test_is_vector(coordinates, expected):
    assert _is_vector(coordinates) == expected

def test_create_vector():
    # assert np.array_equal(create_vector(1, 2, 3), np.array([1, 2, 3, 0]))
    assert _is_close(create_vector((1, 2, 3)), np.array([1, 2, 3, 0]))

def test_is_close():
    assert _is_close(1.0, 1.000001)
    assert not _is_close(1.0, 1.00001)

def test_add_tuples():
    assert _is_close(add_tuples(np.array([1,2,3,1]), np.array([1,1,1,0])), np.array([2,3,4,1]))

def test_substract_tuples():
    assert _is_close(substract_tuples(np.array([1,2,3,1]), np.array([1,1,1,0])), np.array([0,1,2,1])) 

# @pytest.mark.parametrize(
#     "tuples, expected",
#     [
#         (np.array([1, 2, 3, 0]), True),
#         (np.array([1, 2, 3, 1]), False),
#     ],
# )
# def test_add_point_and_vector():  

def test_negate_tuple():
    assert _is_close(negate_tuple(np.array([1,2,3,1])), np.array([-1,-2,-3,-1]))

def test_multiply_tuple():
    assert _is_close(multiply_tuple(np.array([1, -2, 3, -4]), 3.5), np.array([3.5, -7, 10.5, -14]))

def test_divide_tuple():
    assert _is_close(divide_tuple(np.array([1, -2, 3, -4]), 2), np.array([0.5, -1, 1.5, -2]))

def test_magnitude():
    assert _is_close(magnitude(np.array([1, 0, 0, 0])), 1)
    assert _is_close(magnitude(np.array([0, 1, 0, 0])), 1)
    assert _is_close(magnitude(np.array([0, 0, 1, 0])), 1)
    assert _is_close(magnitude(np.array([1, 2, 3, 0])), np.sqrt(14))
    assert _is_close(magnitude(np.array([-1, -2, -3, 0])), np.sqrt(14))

def test_normalize():
    assert _is_close(normalize(np.array([4, 0, 0, 0])), np.array([1, 0, 0, 0]))
    assert _is_close(normalize(np.array([1, 2, 3, 0])), np.array([0.26726, 0.53452, 0.80178, 0]))

def test_dot_product():
    assert _is_close(dot_product(np.array([1, 2, 3, 0]), np.array([2, 3, 4, 0])), 20)

def test_cross_product():
    assert _is_close(np.cross(np.array([1, 2, 3]), np.array([2, 3, 4])), np.array([-1, 2, -1]))
    assert _is_close(np.cross(np.array([2, 3, 4]), np.array([1, 2, 3])), np.array([1, -2, 1]))