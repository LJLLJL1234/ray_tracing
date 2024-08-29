import pytest
import numpy as np

from src.ray_vector import RayVector
from src.utils.utils import _is_close

@pytest.mark.parametrize(
    "xyzp, expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 0], False),
    ],
)
def test_is_point(xyzp, expected):
    vector = RayVector(xyzp)
    assert vector._is_point() == expected

@pytest.mark.parametrize(
    "xyzp, expected",
    [
        ([1, 2, 3, 1], False),
        ([1, 2, 3, 0], True),
    ],
)
def test_is_vector(xyzp, expected):
    vector = RayVector(xyzp)
    assert vector._is_vector() == expected

@pytest.mark.parametrize(
    "xyzp, expected",
    [
        ([1, 2, 3, 1], np.array([1, 2, 3, 1])),
    ],
)
def test_create_vector(xyzp, expected):
    # assert np.array_equal(create_vector(1, 2, 3), np.array([1, 2, 3, 0]))
    assert _is_close(RayVector(xyzp).coords, expected)

@pytest.mark.parametrize(
    "xyzp_1, xyzp_2, expected",
    [
        ([1, 2, 3, 1], [1,1,1,0], np.array([2,3,4,1])),
    ],
)
def test_add_vectors(xyzp_1, xyzp_2, expected):
    assert _is_close((RayVector(xyzp_1) + RayVector(xyzp_2)).coords, expected)

@pytest.mark.parametrize(
    "xyzp_1, xyzp_2, expected",
    [
        ([1, 2, 3, 1], [1,1,1,0], np.array([0,1,2,1])),
    ],
)
def test_subtract_vectors(xyzp_1, xyzp_2, expected):
    assert _is_close((RayVector(xyzp_1) - RayVector(xyzp_2)).coords, expected)

def test_multiply_tuple():
    assert _is_close((RayVector([1, -2, 3, -4]) * 3.5).coords, np.array([3.5, -7, 10.5, -14]))

def test_divide_tuple():
    assert _is_close((RayVector([1, -2, 3, -4]) / 2).coords, np.array([0.5, -1, 1.5, -2]))

@pytest.mark.parametrize(
        "xyzp, expected",
        [
            ([1, 0, 0, 0], 1),
            ([0, 1, 0, 0], 1),
            ([0, 0, 1, 0], 1),
            ([1, 2, 3, 0], np.sqrt(14)),
            ([-1, -2, -3, 0], np.sqrt(14)),
        ]
)
def test_magnitude(xyzp, expected):
    assert _is_close(RayVector(xyzp).magnitude(), expected)

@pytest.mark.parametrize(
        "xyzp, expected",
        [
            ([4, 0, 0, 0], np.array([1, 0, 0, 0])),
            ([1, 2, 3, 0], np.array([0.26726, 0.53452, 0.80178, 0])),
        ],
)
def test_normalize(xyzp, expected):
    assert _is_close(RayVector(xyzp).normalize().coords, expected)
   