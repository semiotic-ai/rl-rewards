# RL Rewards

> [!NOTE]
>
> This is a dramatically oversimplified explanation of RL. Please do not take this as accurate.

In reinforcement learning, agents learn to optimize for some expected return over the course of a game. For example, let's say the agent is learning to go from point A to point B using the best possible path. Path A could have rewards of `[0, 0, 0, 10]`, and path B could have rewards of `[1, 1, 1, 10]`. The sum over each vector gives us our return for each path. Path A has a return of `10` and path B has a return of `13`, making path B a better path that the RL agent should learn.

Identifying which reward function to use for a given problem is extremely difficult in RL. See for instance this old [OpenAI blog post](https://openai.com/index/faulty-reward-functions/). We often want to experiment with which reward function, or combination of reward functions, works best for a given problem.