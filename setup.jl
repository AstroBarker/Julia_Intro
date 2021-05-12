"""
This is an optional setup file to install all dependencies 
and link your Python environment into PyCall.
""" 

using Pkg;

Pkg.add("IJulia")
Pkg.add("Plots")
Pkg.add("BenchmarkTools")
Pkg.add("PyCall")
Pkg.add("PyPlot")
Pkg.add("DataFrames")

# Now we need to link your Python environment.
# The following executes `which python` and grabs the output.

pypath = read( pipeline(`which python`), String )

# pypath will have a newline character at the end. Gotta get rid of that
pypath = strip(pypath, '\n')

# Now set the python environment variable
println( "Setting Python path to: $pypath" )
ENV["PYTHON"] = pypath

# Rebuild PyCall to take effect
Pkg.build("PyCall")