import os

import numpy as np
from pymongo import MongoClient
from pymongo.database import Collection

from constants import (DATABASE_NAME, MONGO_PASSWORD, MONGO_SRV, MONGO_USER)


class EpsilonGreedy:
    def __init__(self, user_id: str, n_arms: int, e: float = 0.01) -> None:
        self.user_id = user_id
        self.n_arms = n_arms
        self.e = e

    @property
    def _collection(self) -> Collection:
        return MongoClient(
            host=os.getenv(MONGO_SRV),
            username=os.getenv(MONGO_USER),
            password=os.getenv(MONGO_PASSWORD),
        )[DATABASE_NAME][self.user_id]

    @property
    def reward_history(self) -> list[list[int]]:
        reward_history = []
        for n in range(self.n_arms):
            reward_history.append(
                [value[str(n)] for value in self._collection.find({str(n): {"$exists": 1}})]
            )

        return reward_history

    def decide(self) -> int:
        reward_history = self.reward_history
        for arm_id in range(self.n_arms):
            if len(reward_history[arm_id]) == 0:
                return arm_id

        if np.random.rand() < self.e:
            return np.random.randint(0, self.n_arms)

        mean_rewards = [np.mean(history) for history in reward_history]
        return int(np.random.choice(
            np.argwhere(mean_rewards == np.max(mean_rewards)).flatten()
        ))

    def update(self, arm_id: int, reward: int) -> None:
        self._collection.insert_one({str(arm_id): reward})
