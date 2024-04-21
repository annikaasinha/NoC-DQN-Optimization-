from environment import NoCEnvironment
from dqn_agent import DQNAgent
import config

def main():
    env = NoCEnvironment(config.env_config)
    agent = DQNAgent(env.observation_space.shape[0], env.action_space.n, config.agent_config)

    for episode in range(config.num_episodes):
        state = env.reset()
        total_reward = 0
        done = False

        while not done:
            action = agent.choose_action(state)
            next_state, reward, done, info = env.step(action)
            agent.remember(state, action, reward, next_state, done)
            agent.replay()
            state = next_state
            total_reward += reward
        
        print(f"Episode {episode + 1}: Total Reward: {total_reward}")

if __name__ == "__main__":
    main()
