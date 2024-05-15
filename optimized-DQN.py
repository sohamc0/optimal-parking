from ray.rllib.algorithms.algorithm import Algorithm
from environment_creation import ParkingLotEnv
from ray.tune.registry import register_env
from ray.rllib.algorithms import dqn
import ray

# Use the Algorithm's `from_checkpoint` utility to get a new algo instance
# that has the exact same state as the old one, from which the checkpoint was
# created in the first place:
my_new_ppo = Algorithm.from_checkpoint('/var/folders/32/zkvyzt8s4_sc6sk_zj9_35zw0000gn/T/tmpsf4owtsq')

# Continue training.
my_new_ppo.train()

	