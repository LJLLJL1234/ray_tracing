import src.utils.utils as utils
import math

a = (1,2,3)
a_point = utils.create_point(a)

print(a_point)

test_vector = utils.create_vector(a)
print(test_vector)
magnitude = utils.magnitude(test_vector)
print(magnitude)
print(math.sqrt(14))

a = utils.create_vector((1,2,3))
b = utils.create_vector((2,3,4))
print(utils.cross_product(a,b))