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

def RK4(f, t0, y0, N, h):
    i = 0
    ti = t0
    yi = y0

    S1 = -1
    S2 = -1
    S3 = -1
    S4 = -1
    yi_1 = -1

    t = [ti]
    y = [yi]

    while(i < N):
        S1 = f(ti, yi)
        S2 = f(ti + h/2, yi + ((h/2) * S1))
        S3 = f(ti + h/2, yi + ((h/2) * S2))

        ti_1 = ti + h
        S4 = f(ti, yi + (h * S3))

        yi_1 = yi + h * (((1/6) * S1) + ((1/3) * S2) + ((1/3) * S3) + ((1/6) * S4))

        ti = ti_1
        yi = yi_1
        i += 1

        t.append(ti)
        y.append(yi)
    
    plt.scatter(t, y)

    return(yi)

def f(t, y):
    return((-20 * y) + (20 * math.sin(t)) + math.cos(t))

calc_exact()
RK4(f, 0, 1, 20, .1)

plt.show()