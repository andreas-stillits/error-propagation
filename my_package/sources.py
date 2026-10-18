"""
Separate module for input types and their sampling functions
"""

from collections.abc import Sequence

import numpy as np


def normal(
    rng: np.random.Generator,
    mean: float,
    std: float,
) -> float:
    """
    Sample from a normal distribution with given mean and standard deviation.
    """
    return rng.normal(loc=mean, scale=std)


def poisson(
    rng: np.random.Generator,
    lam: float,
) -> float:
    """
    Sample from a Poisson distribution with given lambda.
    """
    return rng.poisson(lam=lam)


def empirical(
    rng: np.random.Generator,
    values: Sequence[float | int],
) -> float:
    """
    Sample from an empirical distribution defined by a list of values.
    """
    return rng.choice(values)
