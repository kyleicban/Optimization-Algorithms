import math
from matplotlib import pyplot as plt

def calc_exact():
    def exact(t):
        return(math.sin(t) + (math.e)**(-20 * t))

    t = []
    y = []
    t0 = 0
    for i in range(2000):
        t.append(t0)
        y.append(exact(t0))
        t0 += 0.001

    plt.scatter(t, y)

def eulers(f, t0, y0, N, h):
    i = 0
    ti = t0
    yi = y0
    yi_1 = -1

    t = [ti]
    y = [yi]

    while(i < N):
        yi_1 = yi + (h * f(ti, yi))
        yi = yi_1
        ti += h
        i += 1
        
        t.append(ti)
        y.append(yi)
    
    plt.scatter(t, y)

    return(yi)

def f(t, y):
    return((-20 * y) + (20 * math.sin(t)) + math.cos(t))

calc_exact()
eulers(f, 0, 1, 20, .1)

plt.show()