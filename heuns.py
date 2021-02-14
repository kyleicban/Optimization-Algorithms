import math
from matplotlib import pyplot as plt

def heuns(f, t0, y0, N, h):
    i = 0
    ti = t0
    yi = y0
    yi_1 = -1

    t = [ti]
    y = [yi]

    while(i < N):
        S1 = f(ti, yi)
        S2 = f(ti + h, yi + (h * S1))

        yi_1 = yi + ((h / 2) * (S1 + S2))
        yi = yi_1
        ti += h
        i += 1

        t.append(ti)
        y.append(yi)

    plt.scatter(t, y)

    return(yi)

def f(t, y):
    return(10 * (y - y**2))

heuns(f, 0, 0.5, 500, .01)

plt.show()