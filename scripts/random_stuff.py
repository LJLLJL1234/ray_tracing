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

canvas = Canvas(3, 5)
ppm_header = canvas.canvas_to_ppm()
print(ppm_header)