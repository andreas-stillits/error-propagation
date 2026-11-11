# How to build your Monte Carlo Package - mandatory project part 2

This is an instruction for how to implement your own python package that automates uncertainty propagation. Follow and solve the steps in the order they are presented.

We incourage you to make the code your own - choose names you find meaningful. It will be more fun later if all your packages are slightly different :)

## Prepare your project folder for Part 2
Lets get rid of the files from part 1. Remember you can always restore them using the commit corresponding to when you handed in Assignment 1.

> **TASK:**
>
> 1. Delete the `media/` folder and the `error-propagation.ipynb` notebook with your answers. 
>2. Add the change to Git and commit it.
>3. Move in the new `media/` and `data/` folders for Part 2, together with the `project-exercises.ipynb` notebook. 
>4. Add the change to Git and commit it.

You will use these files to solve exercises using your package. Your folder should now look something like this:

```bash
MandatoryProject/   
    .git/   # hidden folder
    data/
    media/
    project-exercises.ipynb
    instruction-part2.md
```

## Packaging in Python
A minimal package in python is just a folder containing .py files and an additional special `__init__.py` file. This can be empty, and is just telling python that "this is a package". You can have several .py files and subfolder and these can import functionality from each other. Functions you make within the package folder can then be imported into `project-exercises.ipynb` when you later solve exercises.

> **TASK:**
> 
> 1. Create a new folder and give it a name - this will be the name you use when you write `import ...` later.
> 2. Create an empty file called specifically `__init__.py`
> 3. Create another .py file and give it a name - for example `propagation.py`
> 4. Add and commit these changes to Git. 

You should now have something like this:
```bash
MandatoryProject/
    ...
    montecarlo/
        __init__.py
        propagation.py
    ...
```
Here `propagation.py` is the file where you will write the code you intend to reuse.

## Excluding files from Git
When you import functions from a package, python will create a `__pycache__/` folder containing files with the `*.cpython-313.pyc` extension. These are compiled bytecode files that makes loading your package faster on future imports. This is nice, but is tied specifically to *your* machine and with no significance for how your package functions. It is therefore good practice to exclude it from Git version control. We can do that using a `.gitignore` file where we tell Git to ignore all `__pycache__/` folders it can find:

> **TASK:**
>
> 1. Create a `.gitignore` file in your project folder.
> 2. Add: `**/__pycache__/` to the file and save it.
> 3. Add and commit the change to Git. From now on, add and commit changes frequently yourself.

*(If in doubt, see the [course page](https://trusinalab.github.io/DatF_26_27/guides/git/) for more information)*.

## Implementing Monte Carlo Propagation
You are now ready to actually write the code you want to reuse inside your parallel to `propagation.py`. As a quick reminder, the algorithm we want to implement is the following:
 
1. **Define uncertain inputs:** for instance two variables, normal and poisson: $X\sim N(\mu_x,\sigma_x)$ and $Y\sim P(\lambda_y)$
2. **Define a function to propagate the inputs through:** for instance $f(x,y) = x \cdot e^{-y}$
3. **Draw a lot of random input values:** $(x_1, y_1), (x_2, y_2), \cdots,(x_n,y_n)$
4. **Compute the function for each input:** get the sampled distribution $f_1, f_2, \cdots, f_n$

**What changes** from time to time is **what kinds of inputs** we have and the **specific function $f$** we are computing. Your job is to write a function that takes these as arguments and returns the desired $f$ distribution.

### Constraints
While there are lots of different ways this could be implemented, we are going to force you to abide by a few specific choices

#### Managing Randomness
To accomodate scientific reproducibility, your function should take as an argument a random number generator, or at least a random seed. We recommend using NumPy's `numpy.random.Generator` as a strong standard. 
(see examples in Part 1)

#### Managing Inputs
Imagine again a function $f(x,y)$ where $x$ and $y$ are realizations of uncertain variables. Each variable needs a type indication (e.g. is it normal or poisson?) and the parameters needed to specify the distribution. Structure the inputs $f$ needs in a list or dictionary, for example:
```python
inputs = [
    ("normal", 0.0, 1.0), # X is Normal with mean 0 and sigma 1
    ("poisson", 1.0), # Y is Poisson with mean 1
]
```
Your propagation function can then go through `inputs`, recognize the distributions, and generate the random values it needs using NumPy. 

**Specifically, implement these input types:**
- "constant" *(always the same value)*
- "normal" 
- "poisson"
- "empirical" *(a list of possible values/observations to sample from)*

#### Documentation

Your implementation should be well documented so it is easy for others and your future self to understand how it works.  Make sure to add:
- comments throughout your code
- informative docstrings that makes it easy to know how to use your function without looking at its definition
- type hinting: your function's arguments and output should have clear type annotation. For type hinting an argument which is itself a function, you can use: `from collections.abc import Callable`. 

#### Behavior

Overall your function should have a signature that takes in:
- something to generate random numbers
- a specification of the inputs
- a function to propagate inputs through
- a number of samples to draw

And then returns the raw collection of propagated values, not just the mean and standard deviation.

## Time for using it!
Once you have a stable version of your package, go use it to solve the exercises in the `project-exercises.ipynb` notebook. As long as your package folder is in the same directory as the notebook, you should be able to import your function using something like:
```python
from montecarlo.propagation import propagate
```
Go try it out!

### Optionally
You can think of the `from montecarlo.propagation ...` as entering the folders you made - telling python where `propagate()` lives. It is the same thing that happens when you type for instance `from numpy.random import ...`. 
It can however be nice for useself and others using your package that you don't have to worry about that file structure and instead just be able to type: `from montecarlo import propagate`. 

We can achieve this using the `__init__.py` file which has been empty until now. Simply import the propagate function there, and add its name to a special list called `__all__`, for example:

```python
# inside __init__.py

from montecarlo.propagation import propagate
__all__ = ["propagate"]
```

Try it out!