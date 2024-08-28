import pytest

from src.ray_color import RayColor
from src.utils.color_utils import add_colors, subtract_colors, multiply_color
from src.utils.utils import _is_close

def test_ray_color():
    ray_color = RayColor(-0.5, 0.4, 1.7)
    assert _is_close(ray_color.r, -0.5)
    assert _is_close(ray_color.g, 0.4)
    assert _is_close(ray_color.b, 1.7)

def test_color_addition():
    color1 = RayColor(0.9, 0.6, 0.75)
    color2 = RayColor(0.7, 0.1, 0.25)
    result = add_colors(color1, color2)
    assert _is_close(result.r, 1.6)
    assert _is_close(result.g, 0.7)
    assert _is_close(result.b, 1.0)

def test_color_subtraction():
    color1 = RayColor(0.9, 0.6, 0.75)
    color2 = RayColor(0.7, 0.1, 0.25)
    result = subtract_colors(color1, color2)
    assert _is_close(result.r, 0.2)
    assert _is_close(result.g, 0.5)
    assert _is_close(result.b, 0.5)

def test_color_multiplication_with_scalar():
    color1 = RayColor(0.2, 0.3, 0.4)
    c = 2
    result = multiply_color(color1, c)
    assert _is_close(result.r, 0.4)
    assert _is_close(result.g, 0.6)
    assert _is_close(result.b, 0.8)

def test_color_multiplication_with_color():
    color1 = RayColor(1, 0.2, 0.4)
    color2 = RayColor(0.9, 1, 0.1)
    result = multiply_color(color1, color2)
    assert _is_close(result.r, 0.9)
    assert _is_close(result.g, 0.2)
    assert _is_close(result.b, 0.04)

def test_scaled_colors():
    color = RayColor(1.5, 0.5, -1)
    scaled_colors = color.get_scaled_colors()

    assert scaled_colors[0] == 255
    assert scaled_colors[1] == 128
    assert scaled_colors[2] == 0

