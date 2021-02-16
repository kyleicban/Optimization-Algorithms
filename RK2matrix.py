import math
from matplotlib import pyplot as plt
import numpy as np

def calc_exact():
    def exact(t):
        return(((43/36)*math.e**t) + ((1/4)*math.e**(-t)) - ((4/9)*math.e**(-2*t)) + ((1/6)*t*math.e**t))
    
    x = []
    y = []
    x0 = 0
    for i in range(3000):
        x.append(x0)
        y.append(exact(x0))
        x0 += 0.001

    plt.scatter(x, y)

def RK2(A, c, t0, v0, h, N):
    ti = t0
    A = np.array(A)
    vi = np.array(v0)
    vi_1 = np.array([])
    vs = np.array([])
    i = 0

    t = [t0]
    y = [v0[0]]

    while(i < N):
        vs = vi + h*np.dot(A, vi) + h*c(ti)
        vi_1 = vi + (h/2)*np.dot(A,(vi + vs)) + h*c(ti)
        ti = ti + h
        vi = vi_1

        t.append(ti)
        y.append(vi[0])

        i = i + 1

    plt.scatter(t, y)

def c(t):
    return(np.array([0, 0, math.e**t]))

calc_exact()
RK2([[0, 1, 0], [0, 0, 1], [2, 1, -2]], c, 0, [1, 2, 0], 0.1, 30)
plt.show()