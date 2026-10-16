# DatF Mandatory Project - A Monte Carlo Uncertainty Propagation Package

Developed by Andreas Stillits, October 2026 (andreas.stillits@gmail.com) 

## Content

For the first assignment, students will be introduced to the benefits of MC simulation over the familiar error propagation formula via the interactive notebook `error-propagation.ipynb`.
The purpose is to get them excited about learning a new tool that solves a relatable problem - but more importantly how to build a proper, reusable, shareable package that they and others can benefit from.
Over the 4 assignments, they will be introduced to development concepts such as:
- hosting a github repository
- contents of a minimal python package
- git version control
- good documentation
	- README
	- comments
	- docstrings
	- typing
- functions
- classes
- reproducible random number generation
- vectorization with NumPy
- installation into virtual environments with a pyproject.toml file


## Overall Story

"You already solve this problem repeatedly using the error propagation formula. 
First, we will see that it can fail, and that MC simulation can both 
(1) free you of ever differentiating again, and 
(2) even give you more information, i.e. what are the actual distributions, not just $\mu \pm \sigma$ (Part 1). 

Then we automate it with functions (Part 2). 
Then we discover that the automation is too rigid. 

Then we redesign it so other people can use and extend it without modifying your source code (Part 3). 

Finally, we make it fast using parallelism (Part 4)."
