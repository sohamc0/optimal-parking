from environment_creation import ParkingLotEnv
from ray.tune.registry import register_env
from ray.rllib.algorithms.dqn.dqn import DQNConfig
from ray.rllib.algorithms import dqn

def env_creator(env_config):
	return ParkingLotEnv()
	#return ParkingLotEnv(render_mode='human')

register_env("MyGrid", env_creator)

config = DQNConfig()


replay_config = {
        "type": "MultiAgentPrioritizedReplayBuffer",
        "capacity": 60000,
        "prioritized_replay_alpha": 0.6,
        "prioritized_replay_beta": 0.4,
        "prioritized_replay_eps": 1e-06,
    }


config = config.training(replay_buffer_config=replay_config)
config = config.rollouts(num_rollout_workers=2)
config = config.resources(num_gpus=0)
config = config.env_runners(num_env_runners=1)
config = config.environment("MyGrid")

algo = dqn.DQN(config=config)

for _ in range(10):
	algo.train()

save_result = algo.save()
path_to_checkpoint = save_result.checkpoint.path
print(
    "An Algorithm checkpoint has been created inside directory: "
    f"'{path_to_checkpoint}'."
)