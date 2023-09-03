""" NO COMMITEAR ESTE ARCHIVO!"""
""" Roud-robin tournament between agents with both colors and trueskill rating"""

# Import the agents
import time
from itertools import permutations

import gymnasium as gym
import tqdm
import trueskill
from tournament_utils import print_results
import gomoku_udesa
import numpy as np
# **Import the agents HERE!**
from agents.schuemer.optimizedAgent import SchuemerAgent
from agents.schuemer.randomAgent import RandomAgent
from agents.schuemer.videla_agent import VidelaAgent


class consoleAgent:
    def __init__(self):
        pass

    def action(self, board):
        action = input("Enter action: ")
        action = action.split()
        action = (int(action[0])*board.shape[0]) + int(action[1])
        return action
    

# **Add the agents to the list HERE!**
agents = {
    # RandomAgent(),
    # consoleAgent(),
    SchuemerAgent(),
    VidelaAgent(),
    
}
ROUNDS = 1
SIZE = 15

env = gym.make(
    "gomoku_udesa/Gomoku-v0",
    render_mode="human",
    max_episode_steps=SIZE * SIZE + 1,
    num_rows=SIZE,
    num_cols=SIZE,
    num_in_row=5,
)  


for agent in agents:
    agent.rating = trueskill.Rating()

for agent1, agent2 in tqdm.tqdm(list(permutations(agents, 2)) * ROUNDS):
    board, _ = env.reset()
    terminated, truncated = False, False
    time1, time2, n = 0, 0, 0
    while not terminated and not truncated:
        if n % 2 == 0:
            start = time.perf_counter()
            action = agent1.action(board)
            time1 += time.perf_counter() - start
            board, reward1, terminated, truncated, info = env.step(action)
        else:
            start = time.perf_counter()
            action = agent2.action(-board)
            time2 += time.perf_counter() - start
            board, reward2, terminated, truncated, info = env.step(action)
        n += 1
        env.render()
        time.sleep(0)
    time.sleep(3)

    agent1.time = time1 / (n / 2)
    agent2.time = time2 / (n / 2)

    if reward1 == 1:
        agent1.rating, agent2.rating = trueskill.rate_1vs1(agent1.rating, agent2.rating)
    elif reward2 == 1:
        agent2.rating, agent1.rating = trueskill.rate_1vs1(agent2.rating, agent1.rating)
    else:
        agent1.rating, agent2.rating = trueskill.rate_1vs1(
            agent1.rating, agent2.rating, drawn=True
        )

print_results(agents)
