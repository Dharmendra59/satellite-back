import gymnasium as gym
import numpy as np
from gymnasium import spaces

class SpaceEnv(gym.Env):
    def __init__(self):
        super().__init__()

        # 🔹 State: [distance_to_debris, relative_velocity]
        self.observation_space = spaces.Box(
            low=0, high=20000, shape=(2,), dtype=np.float32
        )

        # 🔹 Actions: altitude change (-1, 0, +1)
        self.action_space = spaces.Discrete(3)

        self.distance = 10000
        self.velocity = 7.5

    def reset(self, seed=None, options=None):
        self.distance = np.random.uniform(3000, 12000)
        self.velocity = np.random.uniform(6, 8)
        return np.array([self.distance, self.velocity]), {}

    def step(self, action):
        # Action effect
        if action == 0:      # DOWN
            self.distance -= 200
        elif action == 2:    # UP
            self.distance += 200

        # Risk & reward
        done = False
        reward = 0

        if self.distance < 1000:
            reward = -100   # 💥 collision
            done = True
        else:
            reward = 10 - abs(action - 1)  # fuel penalty

        state = np.array([self.distance, self.velocity])
        return state, reward, done, False, {}
