import pytest
import numpy as np
# import sys
# sys.path.append('/Users/Lauri.Lehtola/private_projects/ray_tracing')
from src.utils.utils import _is_point, create_point, _is_vector, create_vector, _is_close, add_tuples, substract_tuples

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