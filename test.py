import numpy as np

A = np.array([[1, 0, 1], [0, 1, 0], [0, 0, 1]])
print(np.linalg.solve(A, [1, 2, 3]))
