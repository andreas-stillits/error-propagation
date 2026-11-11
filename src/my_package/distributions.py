import numpy as np

from .sources import Source


class Normal(Source):
    def __init__(self, mean: float, std: float):
        self.mean = mean
        self.std = std

    def sample(self, rng: np.random.Generator) -> float:
        return rng.normal(self.mean, self.std)


class Poisson(Source):
    def __init__(self, lam: float):
        self.lam = lam

    def sample(self, rng: np.random.Generator) -> int:
        return rng.poisson(self.lam)


class Uniform(Source):
    def __init__(self, low: float, high: float):
        self.low = low
        self.high = high

    def sample(self, rng: np.random.Generator) -> float:
        return rng.uniform(self.low, self.high)
