#!/usr/bin/env julia

"""
This is okay!
Returns Hilbert matrix of size n
"""
function Hilbert_dynamic( n )
  matrix = zeros( n, n )

  for i in 1:n
    for j in 1:n
      matrix[i,j] = 1.0 / ( i + j - 1.0 )
    end
  end

  return matrix
end


"""
This is better!
Returns Hilbert matrix of size n
"""
function Hilbert_static( n::Int64 )
  matrix::Array{Float64, 1} # or Vector{Float64}

  for i in 1:n
    for j in 1:n
      matrix[i,j] = 1.0 / (i + j - 1.0)
    end
  end
  
  return matrix
end


println( Hilbert_dynamic(3) )
