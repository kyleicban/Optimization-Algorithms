import math
from matplotlib import pyplot as plt

def RK4(f, t0, y0, N, h):
    i = 0
    ti = t0
    yi = y0

    S1 = -1
    S2 = -1
    S3 = -1
    S4 = -1
    yi_1 = -1

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

    return(yi)

def calc_exact():
    def exact(t):
        return(t**2 + ((1/3) * math.e**(-5 * t)))

    t = []
    y = []
    t0 = 0
    for i in range(1000):
        t.append(t0)
        y.append(exact(t0))
        t0 += 0.001

    plt.scatter(t, y)

def AB2(f, t0, y0, N, h):
    i = 0
    ti_p = t0 # t_i-1, abbreviated to ti_previous
    yi_p = y0 # y_i-1, abbreviated to yi_previous
    ti = t0 + h
    yi = RK4(f, t0, y0, 1, h)
    yi_1 = -1

    t = [ti]
    y = [yi]

    N = N - 1

    while(i < N):
        ti_1 = ti + h
        yi_1 = yi + h * ((1.5 * f(ti, yi)) - 0.5 * f(ti_p, yi_p))
        ti_p = ti
        yi_p = yi
        ti = ti_1
        yi = yi_1
        i += 1

        t.append(ti)
        y.append(yi)
    

    plt.scatter(t, y)

    return(yi)

def f(t, y):
    return(-5 * y + 5 * t**2 + 2 * t)

calc_exact()
AB2(f, 0, 1/3, 10, .1)

plt.show()