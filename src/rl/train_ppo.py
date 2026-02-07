from stable_baselines3 import PPO
from src.rl.env import SpaceEnv

env = SpaceEnv()

model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    learning_rate=0.0003,
    gamma=0.99
)

model.learn(total_timesteps=50000)
model.save("ppo_satellite")
