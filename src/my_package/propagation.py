from collections.abc import Callable, Sequence
from typing import Any

import numpy as np

from .sources import Source


def propagate(
    rng: np.random.Generator,
    func: Callable[..., Any],
    inputs: Sequence[Source],
    n_samples: int = 1_000,
) -> list[Any]:
    """
    Propagates uncertainty through the supplied function by sampling from the input distributions.

    Args:
        rng (np.random.Generator): A random number generator.
        func (Callable[..., Any]): The function to propagate uncertainty through.
        inputs (Sequence[Source]): A sequence of Source objects representing the input distributions.
        n_samples (int, optional): The number of samples to draw from the input distributions. Defaults to 1_000.

    Returns:
        list[Any]: A list of the results of the function applied to the sampled input values.
    """
    # initialize empty container
    results = []
    for _ in range(n_samples):
        sampled_inputs = [
            source.sample(rng) for source in inputs
        ]  # sample from the input distributions - what we acheived is that we just call source.sample(rng) REGARDLESS of its behavior
        result = func(*sampled_inputs)  # evalue the function with the sampled inputs
        results.append(result)  # store the result
    return results  # return the result
