# Copyright 2025-, Semiotic AI, Inc.
# SPDX-License-Identifier: Apache-2.0

# In this exercise, we intentionally don't use numpy or any third party packages to avoid setup issues. You're welcome to pip install them yourself if you'd like.
# We also work in a single file for convenience instead of creating a lib with a separate tests folder. Again, to avoid pytest or some external dep.
# To run any test, you can run `python main.py function_name` from the commandline

# We want to teach our agent to play capture the flag. Assume at this point it has acquired the flag and is trying to run back to base. We want to keep track of our experiments with different reward functions, so we use config files to specify our reward functions.

#### HELPERS ####
import sys

def l2_distance(source: list[float], dest: list[float]) -> float:
    if len(source) != len(dest):
        raise ValueError("Lists must be of the same length")

    distance = 0.0
    for a, b in zip(source, dest):
        distance += (a - b) ** 2

    return distance ** 0.5

#### YOUR CODE HERE ####
def compute_reward(config: list[dict]) -> float:
    return 0.0

def test_run_straight_back_to_base_reward():
    agent_pos = [0.0, 0.0]
    homebase_pos = [3.0, 4.0]
    reward_config = [
        {}  # fill in
    ]
    reward = compute_reward(reward_config)
    assert reward == -5.0  # why should this be negative?

def test_reward_only_when_at_base():
    agent_pos = [0.0, 0.0]
    homebase_pos = [0.0, 0.0]
    reward_config = [
        {}  # fill in
    ]
    reward = compute_reward(reward_config)
    assert reward == 100.0

def test_reward_max_dist_from_defender():
    agent_pos = [2.0, 2.0]
    defender_pos = [2.0, 5.0]
    reward_config = [
        {}  # fill in
    ]
    reward = compute_reward(reward_config)
    assert reward == 3.0

def test_all_rewards_combined():
    agent_pos = [0.0, 0.0]
    homebase_pos = [3.0, 4.0]
    defender_pos = [0.0, 3.0]
    reward_config = [
        {}  # fill in
    ]
    reward = compute_reward(reward_config)
    assert reward == -2.0

if __name__ == "__main__":
    globals()[sys.argv[1]]()
