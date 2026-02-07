import numpy as np
import random

def get_debris_position(sat_position):
    offset = random.uniform(1, 10)  # km
    return np.array([
        sat_position[0] + offset,
        sat_position[1] - offset,
        sat_position[2] + offset
    ])
