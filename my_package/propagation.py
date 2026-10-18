"""
Third implementation with functions
___________________________________

- with typing
- with docstrings
- with module separation
___________________________________

Basic idea:

- define an input as a list of tuples
- each tuple contains:
    - a type identifier (string)
    - values/parameters that define the input
- the core function runs a loop over the input list
  and calls the appropriate function based on the identifier
- the outputs are finally collected and returned as a list

"""

from collections.abc import Callable
from typing import Any

import numpy as np

from my_package.sources import empirical, normal, poisson


def propagate(
    rng: np.random.Generator,
    func: Callable[..., float],
    inputs: list[tuple[Any, ...]],
    n_samples: int = 10_000,
) -> list[float]:
    """
    Propagate uncertainty through a function.
    Provide a numpy random number generator, a function to propagate, a list of function inputs, and a number of samples to draw.

    Arguments:
    - rng: a numpy random number generator
    - func: a function to propagate, which takes a tuple of floats and returns a float
    - inputs: a list of tuples, where each tuple contains:
        - a string identifier for the input type ("constant", "normal", "poisson", or "empirical")
        - the parameters for the input type (e.g., mean and std for normal, lambda for poisson, or a list of values for empirical)
    - n_samples: the number of samples to draw from the input distributions

    Returns:
    - a list of floats, which are the outputs of the function for each sample drawn from the input distributions

    Raises:
    - ValueError: if an unknown input type is provided
    """

    outputs: list[float] = []

    # loop over the number of samples
    for _ in range(n_samples):
        sample: list[float] = (
            []
        )  # list to hold the sampled values that goes into func (in order)

        # loop over the inputs and sample values based on the input type
        for input_type, *params in inputs:

            # if constant, just take the value
            if input_type == "constant":
                value = params[0]
                sample.append(value)

            # if normal, pass the mean and std to the rng.normal function
            elif input_type == "normal":
                sample.append(normal(rng, *params))

            # if poisson, pass the lambda parameter to the rng.poisson function
            elif input_type == "poisson":
                sample.append(poisson(rng, *params))

            # if empirical, sample from the provided data using rng.choice
            elif input_type == "empirical":
                sample.append(empirical(rng, *params))

            # raise an error if the input type is unknown
            else:
                raise ValueError(f"Unknown input type: {input_type}")

        outputs.append(func(*sample))

    return outputs
