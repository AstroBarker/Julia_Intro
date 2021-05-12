# Simple upwind advection solver
# Only implements tophat, only on interva; 0 to 1

# using PyPlot

function Init_Cond( N::Int64, shape::String )
  """
  Set initial conditions for size and shape
  """

  x :: Vector{Float64} = zeros( N )
  a :: Vector{Float64} = zeros( N )

  @inbounds @simd for i in 1:N
    x[i] = (i-1) / (N-1)
    if ( shape == "tophat" )
      if (x[i] >= 0.35 && x[i] <= 0.65)
        a[i] = 1.0
      end
    else
      error("Only implemented tophat")
    end
  end

  return x, a

end


function Evolve( a::Vector{Float64}, new::Vector{Float64}, u::Float64, CFL::Float64, method::String )

  N = length(a)
  if ( u > 0.0 ) # periodic BC
    a[1] = a[N]
  else
    a[N] = a[1]
  end

  @inbounds @fastmath for i in 2:N
    new[i] = a[i] .- CFL .*  ( a[i] .- a[i-1] )
  end

  @inbounds @simd for i in 1:N
    a[i] = new[i]
  end

end


function Integrator( a::Vector{Float64}, work::Vector{Float64}, u::Float64, CFL::Float64,
  t::Float64, tend::Float64, dt::Float64, method::String )

  while ( t < tend )

    if ( t + dt <= tend )
      Evolve( a, work, u, CFL, method )
    end
    t += dt

  end

end


function Solve( N::Int64 )

  dx :: Float64 = 1.0 / (N-1.0)
  C  :: Float64 = 1.0
  u  :: Float64 = 0.1
  dt :: Float64 = C * dx / abs(u)

  tend :: Float64 = 10.0

  shape :: String = "tophat"

  x, a = Init_Cond( N, shape )

  work :: Vector{Float64} = zeros( N )

  Integrator( a, work, u, C, 0.0, tend, dt, "upwinding" )

  # _, ic = Init_Cond( N, shape )
  # plot( x, a )
  # plot(x, ic, label="Initial", ls="--", lw="1.5", color="k")
  # show()

end


# Solve(100)