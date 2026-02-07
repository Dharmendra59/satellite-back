import numpy as np

def distance_km(pos1, pos2):
    return np.linalg.norm(np.array(pos1) - np.array(pos2))
