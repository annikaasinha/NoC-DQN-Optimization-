import gym
from gym import spaces
import numpy as np

class NoCEnvironment(gym.Env):
    metadata = {'render.modes': ['console']}

    def __init__(self, config):
        super(NoCEnvironment, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        self.action_space = spaces.Discrete(4)  # e.g., four actions
        self.observation_space = spaces.Box(low=0, high=255, shape=(10,), dtype=np.float32)  # e.g., ten measurements

    def step(self, action):
        # Execute one time step within the environment
        next_state = np.random.rand(10) * 255
        reward = -1 if action == 0 else 1  # Dummy reward
        done = np.random.rand() > 0.95
        return next_state, reward, done, {}

    def reset(self):
        # Reset the state of the environment to an initial state
        return np.random.rand(10) * 255

    def render(self, mode='console'):
        if mode != 'console':
            raise NotImplementedError()
        # Print the current state
        print("Current state:", self.state)

    def close(self):
        pass

