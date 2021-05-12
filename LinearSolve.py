import numpy as np

def LinearSolve( size ):
  """
  Set up and solve a lienar sytstem of size n with solution np.ones(size)
  """

  matrix = np.ones( (size, size) )
  matrix += np.identity( size )
  
#   x = np.ones( size )

#   y = np.matmul( matrix, np.ones( size ) )

  return np.linalg.solve( matrix, np.ones( size ) )

