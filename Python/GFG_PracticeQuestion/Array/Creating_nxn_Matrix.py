#Creating an n×n matrix efficiently.
# 1. Nested List
# 2. Loop
# 3. Numpy

# import numpy
# n = 4
# matrix = numpy.ones((n,n),dtype=int)
# print(matrix)

# 4. Pandas Library
# import pandas as pd

# # Create a 3x3 matrix with labeled rows and columns
# n = 3
# matrix = pd.DataFrame([[i * n + j + 1 for j in range(n)] for i in range(n)],
#                     columns=['A', 'B', 'C'])
# print(matrix)