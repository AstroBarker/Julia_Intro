'''
Simple python advection solver. 1D, only tophat profile, upwinding.
'''

import numpy as np
import time
from numba import njit
# import matplotlib.pyplot as plt

@njit
def init_cond( N, shape ):
    """
    set an initial condition
    N : number of (equidistant) points
    shape : "tophat" or "Gaussian" -- exactly
    """

    x = np.linspace( 0.0, 1.0, N )
    a = np.zeros_like( x )

    if ( shape == "tophat"):
        a[(x >=0.35) & (x<=0.65)] = 1.0
        # for i in range( N ):
            # if (x[i] >= 0.35 and x[i] <= 0.65):
                # a[i] = 1.0
    elif( shape == "Gaussian" ):
        sigma = 0.1 / (2.0*np.sqrt(2.0*np.log(2)))
        mu = 0.5
        a = (1.0 / (sigma * np.sqrt(2.0*np.pi))) * \
            np.exp( -(x - mu)**2 / (2.*sigma**2) )
    else:
        raise ValueError("tophat or Gaussian only -- exactly like here.")
    
    return x, a


@njit
def evolve( a, u, CFL, method ):

    a[0] = a[-1] # periodic BC
    n = len(a)
    new = np.zeros_like(a)#np.copy(a)
    if (method == "upwinding"):
        new[1:n] = a[1:n] - CFL * ( a[1:n] - a[0:n-1] )
    elif (method == "FTCS"):
        new[1:n-1] = a[1:n-1] - 0.5*CFL * ( a[2:n] - a[0:n-2] )
        new[n-1] = a[n-1] = 0.5*CFL * ( a[0] - a[n-2])
    else:
        raise ValueError(" i already warned you once about the method types .,.,...")
    a[:] = new[:]


@njit
def integrator( a, u, CFL, t, tend, dt, method ):
    """
    integrate PDE
    """

    while (t < tend):

        if ( t + dt <= tend ):
            evolve( a, u, CFL, method )
        
        t += dt



def plot( x, a, CFL, t, N, shape, method ):

    _, ic = init_cond( N, shape=shape )
    
    fig, ax = plt.subplots(figsize=(10,10))
    ax.plot(x, ic, label="Initial", ls="--", lw="1.5", color="k")
    ax.plot(x, a, label=f"t={t}", alpha=0.4)
    ax.set(xlabel = "x", ylabel="a(x)", title=f"CFL = {CFL}, t = {t}")
    ax.legend(frameon=True)
    plt.show()
    fn = "advection_CFL" + str(CFL) + "_t" + str(t) + "_" + shape + "_"  + str(method) + ".png"
    # fig.savefig( fn )


@njit
def Solve( N ):


    dx = 1.0 / (N-1)
    C = 1.0
    u = 0.1
    dt = C * dx / np.abs( u )
    tend = 10.0
    shape = "tophat"
    method = "upwinding"

    x, a = init_cond( N, shape=shape )
    # evolve( a, 0.1, 10.0, "upwinding")
    integrator( a, u, C, 0.0, tend, dt, method )
    # plot(x, a, C, tend, N, shape, method)



if __name__ == '__main__':

    num_runs = 1000

    sizes = [ 128, 256, 512, 1024, 2048, 4096, 8192 ]
    for i in range(len(sizes)):

        times = []

        Solve(100)
        for num in range(num_runs):

            t0 = time.time()
            Solve(sizes[i])
            t1 = time.time()
            times.append( t1-t0 )
        print( np.average(times) )