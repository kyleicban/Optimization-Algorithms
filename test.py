import numpy as np

A = np.array([[1, 0, 1], [0, 1, 0], [0, 0, 1]])
print(np.linalg.solve(A, [1, 2, 3]))

print(A)
print(np.tril(A, -1))
print(np.triu(A, 1))
print(np.diag(np.diag(A)))
print(np.linalg.inv(np.diag(np.diag(A))))
