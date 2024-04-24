# NoC-DQN-Optimization

This repository hosts the **NoC-DQN-Optimization** project, which applies reinforcement learning to optimize the performance of network-on-chip (NoC) configurations. The project focuses on enhancing latency, bandwidth, and power efficiency in complex system-on-chip (SoC) designs using a Deep Q-Network (DQN).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This will run on Python 3.6+.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/YourGitHubUsername/NoC-DQN-Optimization.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd NoC-DQN-Optimization
   ```

3. **Install required Python libraries:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main simulation with:

```bash
python main.py
```

This command initiates the DQN-based optimization process on the defined NoC simulation environment.

## Project Structure

- `main.py`: The entry point of the simulation.
- `dqn_agent.py`: Implements the DQN agent.
- `environment.py`: Defines the NoC simulation environment.
- `config.py`: Contains configuration settings.
- `requirements.txt`: Lists the project dependencies.

