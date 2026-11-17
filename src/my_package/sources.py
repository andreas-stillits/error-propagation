from collections.abc import Callable, Sequence
from typing import Any

import numpy as np


class Source:
    def sample(self, rng: np.random.Generator):
        raise NotImplementedError("Subclasses must implement the sample method.")


class Constant(Source):
    def __init__(self, value: Any):
        self.value = value

    def sample(self, rng: np.random.Generator) -> Any:
        return self.value


class Empirical(Source):
    def __init__(self, value: Sequence[Any]):
        self.value = value

    def sample(self, rng: np.random.Generator) -> Any:
        index = rng.integers(0, len(self.value))
        return self.value[index]


class Model(Source):
    def __init__(self, model: Callable[[np.random.Generator], Any]):
        self.model = model

    def sample(self, rng: np.random.Generator) -> Any:
        return self.model(rng)
