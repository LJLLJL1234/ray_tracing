import pytest
import numpy as np
from src.utils import _is_point, create_point, _is_vector, create_vector, _is_close

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
    assert np.array_equal(create_point(1, 2, 3), np.array([1, 2, 3, 1]))
                          
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
    assert _is_close(create_vector(1, 2, 3), np.array([1, 2, 3, 0]))

def test_is_close():
    assert _is_close(1.0, 1.000001)
    assert not _is_close(1.0, 1.00001)