from environment_creation import ParkingLotEnv
from ray.tune.registry import register_env
from ray.rllib.algorithms.ppo import PPOConfig

def env_creator(env_config):
	#return ParkingLotEnv()
	return ParkingLotEnv(render_mode='human')

register_env("MyGrid", env_creator)

config = PPOConfig()
config = config.rollouts(num_rollout_workers=2)
#config = config.training(gamma=0.999, lr=0.001)
algo = config.build(env="MyGrid")

for _ in range(10):
	algo.train()


save_result = algo.save()
path_to_checkpoint = save_result.checkpoint.path
print(
    "An Algorithm checkpoint has been created inside directory: "
    f"'{path_to_checkpoint}'."
)
