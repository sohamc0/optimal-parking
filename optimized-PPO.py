from ray.rllib.algorithms.algorithm import Algorithm
from environment_creation import ParkingLotEnv
from ray.tune.registry import register_env
from ray.rllib.algorithms.ppo import PPOConfig

# Use the Algorithm's `from_checkpoint` utility to get a new algo instance
# that has the exact same state as the old one, from which the checkpoint was
# created in the first place:

def env_creator(env_config):
	#return ParkingLotEnv()
	return ParkingLotEnv(render_mode='human')

register_env("MyGrid", env_creator)

config = PPOConfig()
config = config.rollouts(num_rollout_workers=2)
my_new_ppo = config.build(env="MyGrid")

my_new_ppo = Algorithm.from_checkpoint('/var/folders/32/zkvyzt8s4_sc6sk_zj9_35zw0000gn/T/tmpcu84wqys')

# Continue training.
my_new_ppo.train()

	