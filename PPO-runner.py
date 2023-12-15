from environment_creation import ParkingLotEnv
from ray.tune.registry import register_env
from ray.rllib.algorithms import ppo
import ray

def env_creator(env_config):
	return ParkingLotEnv()

register_env("MyGrid", env_creator)

ray.init()

algo = ppo.PPO(env="MyGrid")

for _ in range(10):
	algo.train()

