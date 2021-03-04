import math
from matplotlib import pyplot as plt
import numpy as np

def l_2(v):
    ret = 0
    for vi in v:
        ret += abs(vi)**2
    return(math.sqrt(ret))

def gauss_seidel(A, b, x0, eps):
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    D = np.diag(np.diag(A))
    D_inv = np.linalg.inv(D)

    k = 1
    xk_1 = x0

    rk = b - (np.dot(A, x0))
    rk = list(rk)
    normrk = l_2(rk)

    r_list = []
    k_list = []

    LD_inv = np.linalg.inv(L + D)
    LD_invb = np.dot(LD_inv, b)
    LD_invU = np.dot(LD_inv, U)

    while normrk > eps:
        r_list.append(normrk)
        k_list.append(k)

        xk = LD_invb - np.dot(LD_invU, xk_1)

        rk = b - (np.dot(A, xk))
        rk = list(rk)
        normrk = l_2(rk)

        xk_1 = xk

        k += 1
    
    plt.scatter(k_list, r_list)
    print("There were " + str(k - 1) + " iterations.")

A = [
    [4, -1, 0, -1, 0, 0],
    [-1, 4, -1, 0, -1, 0],
    [0, -1, 4, 0, 0, -1],
    [-1, 0, 0, 4, -1, 0],
    [0, -1, 0, -1, 4, -1],
    [0, 0, -1, 0, -1, 4],    
]
A = np.array(A)

b = [2, 1, 2, 2, 1, 2]
b = np.array(b)

x0 = [0, 0, 0, 0, 0, 0]
x0 = np.array(x0)

gauss_seidel(A, b, x0, 0.01)

plt.show()