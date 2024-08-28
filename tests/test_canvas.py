from src.canvas import Canvas
from src.ray_color import RayColor
from src.utils.utils import _is_close

def test_canvas():
    canvas = Canvas(10, 20)
    assert _is_close(canvas.width, 10)
    assert _is_close(canvas.height, 20)
    for x in range(10):
        for y in range(20):
            assert canvas.get_pixel(x, y) == RayColor(0,0,0)

def test_set_pixel_color():
    canvas = Canvas(10,20)
    color = RayColor(1,0,0)
    canvas.write_pixel(2, 3, color)
    assert canvas.get_pixel(2,3) == color

def test_ppm_header():
    canvas = Canvas(5, 3)
    ppm = canvas.canvas_to_ppm()
    lines = ppm.splitlines()
    test_lines = "\n".join(lines[:3])
    assert test_lines == "P3\n5 3\n255"

def test_ppm_body():
    canvas = Canvas(5, 3, ppm_split=32)
    canvas.write_pixel(0,0,RayColor(1.5, 0, 0))
    canvas.write_pixel(2,1,RayColor(0, 0.5, 0))
    canvas.write_pixel(4, 2, RayColor(-0.5, 0, 1))

    expected_body = """255 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 128 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"""
    test_ppm = "\n".join(canvas.canvas_to_ppm().splitlines()[3:])
    # test_body = "\n".join(test_ppm.splitlines()[3:])
    assert test_ppm == expected_body
