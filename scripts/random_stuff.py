import src.utils.utils as utils
import math
from src.ray_color import RayColor
from src.utils.color_utils import multiply_color
from src.canvas import Canvas

# a = (1,2,3)
# a_point = utils.create_point(a)

# print(a_point)

# test_vector = utils.create_vector(a)
# print(test_vector)
# magnitude = utils.magnitude(test_vector)
# print(magnitude)
# print(math.sqrt(14))

# a = utils.create_vector((1,2,3))
# b = utils.create_vector((2,3,4))
# print(utils.cross_product(a,b))

# color1 = RayColor(1, 0.2, 0.4)
# color2 = RayColor(0.9, 1, 0.1)
# result = multiply_color(color1, color2)

# print(result)

canvas = Canvas(5, 3, ppm_split=32)
canvas.write_pixel(0,0,RayColor(1.5, 0, 0))
canvas.write_pixel(2,1,RayColor(0, 0.5, 0))
canvas.write_pixel(4, 2, RayColor(-0.5, 0, 1))

expected_body = """255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n
                    0 0 0 0 0 0 0 128 0 0 0 0 0 0 0\n
                    0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"""
test_ppm = "\n".join(canvas.canvas_to_ppm().splitlines()[3:])
print("Test ppm: ")
print(test_ppm)
print("Expected:")
print(expected_body)
# test_body = "\n".join(test_ppm.splitlines()[3:])

# print(test_ppm)
# print("#############")
# print(test_body)
# print("#############")
# test_ppm = "\n".join(canvas.canvas_to_ppm().splitlines()[3:])
# print(test_ppm)