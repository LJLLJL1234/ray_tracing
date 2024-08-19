import src.utils.utils as utils

position = utils.create_point((0, 1, 0))
velocity = utils.create_vector((1, 1, 0))

gravity = utils.create_vector((0, -0.1, 0))
wind = utils.create_vector((-0.01, 0, 0))

while True:
    position = utils.add_tuples(position, velocity)
    velocity = utils.add_tuples(velocity, utils.add_tuples(gravity, wind))
    print("Position: ", position)
    print("Velocity: ", velocity)

    if position[1] <= 0:
        break