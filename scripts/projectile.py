import src.utils.utils as utils
from src.canvas import Canvas
from src.ray_color import RayColor

position = utils.create_point((0, 1, 0))
velocity = utils.normalize(utils.create_vector((1, 1.8, 0))) * 11.25

gravity = utils.create_vector((0, -0.1, 0))
wind = utils.create_vector((-0.02, 0, 0))

position_list = []
position_list.append(utils.round_to_int(position))

while True:
    position = utils.add_tuples(position, velocity)
    velocity = utils.add_tuples(velocity, utils.add_tuples(gravity, wind))
    # print("Position: ", position)
    # print("Velocity: ", velocity)
    
    if position[1] <= 0:
        break
    position_list.append(utils.round_to_int(position))

# print(position_list)
p_color = RayColor(0.5, 0.5, 0.5)
canvas = Canvas(900, 550)
for p in position_list:
    x = p[0]
    y = 550 - p[1]
    print(f"x: {x}, y: {y}")
    canvas.write_pixel(x, y, p_color)
    for i in range(-2, 3):
        for j in range(-2, 3):
            x_mod = x+i
            y_mod = y + j
            if 0 < x_mod < 900 and 0 < y_mod < 550:
                canvas.write_pixel(x_mod, y_mod, p_color)

canvas.save_ppm_file()

