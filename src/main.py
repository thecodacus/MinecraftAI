import minerl
import gym
import logging
logging.basicConfig(level=logging.DEBUG)

env = gym.make('MineRLNavigateDense-v0')

# env.make_interactive(port=6666, realtime=True)

obs  = env.reset()
done = False
net_reward = 0

while not done:
    env.render()
    action = env.action_space.noop()

    action['camera'] = [0, 0.03*obs["compass"]["angle"]]
    action['back'] = 0
    action['forward'] = 1
    action['jump'] = 1
    action['attack'] = 1

    obs, reward, done, info = env.step(
        action)

    net_reward += reward
    print("Total reward: ", net_reward)