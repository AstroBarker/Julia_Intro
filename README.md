# Intro to Julia

This repo has some basics I put together to introduce colleagues to the Julia programming language.
They are not meant to be comprehensive, focusing on overarching themes and introducing syntax for some common use cases.
More resources are listed in [resources.md](resources.md).

If you do not yet have Julia, [download it](https://julialang.org/downloads/).
You may want to alias the Julia executable `alias julia='/path/to/julia/bin/julia'`.
On my Mac, the path looks like this `alias julia='/Applications/Julia-1.6.app/Contents/Resources/julia/bin/julia'` (more complciated than on linux systems).
I'll assume this command is available to you.
To use this resource you don't need any dependencies already installed except `IJulia`.
If you do not yet have this, enter the julia REPL by typing `julia` at the command line.
Once there you may type `]` to enter the package manager mode followed by `add IJulia` or `using Pkg` following by `Pkg.add("IJulia)`.
`exit()` to exit.
All other dependencies may be installed in the notebook.

Alternatively, the script `setup.jl` can be ran with `julia setup.jl` and will install all the packages used here and set Julia to use your Python installation.

We will use:
* [Plots](https://docs.juliaplots.org/latest/)
* [BenchmarkTools](https://juliapackages.com/p/benchmarktools)
* [PyCall](https://juliapackages.com/p/pycall)
* [PyPlot](https://juliapackages.com/p/pyplot)
* [DataFrames](https://juliapackages.com/p/dataframes)