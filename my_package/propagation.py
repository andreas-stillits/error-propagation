"""
First implementation with functions
___________________________________

- no typing
- no docstrings
- no module separation
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


def propagate(rng, func, inputs, n_samples=1_000):
    outputs = []

    # loop over the number of samples
    for _ in range(n_samples):
        sample = []  # list to hold the sampled values that goes into func (in order)

        # loop over the inputs and sample values based on the input type
        for input_type, *params in inputs:

            # if constant, just take the value
            if input_type == "constant":
                value = params[0]
                sample.append(value)

            # if normal, pass the mean and std to the rng.normal function
            elif input_type == "normal":
                value = rng.normal(loc=params[0], scale=params[1])
                sample.append(value)

            # if poisson, pass the lambda parameter to the rng.poisson function
            elif input_type == "poisson":
                value = rng.poisson(lam=params[0])
                sample.append(value)

            # if empirical, sample from the provided data using rng.choice
            elif input_type == "empirical":
                data = params[0]
                value = rng.choice(data, replace=True)
                sample.append(value)

            # raise an error if the input type is unknown
            else:
                raise ValueError(f"Unknown input type: {input_type}")

        outputs.append(func(*sample))

    return outputs
