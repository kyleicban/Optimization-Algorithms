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

# trapozoidal specifically for problem 1 on HW4
def trapezoidal(f, t0, y0, N, h):
    i = 0
    ti = t0
    yi = y0

    yi_1 = -1

    t = [ti]
    y = [yi]

    while(i < N):
        ti_1 = ti + h

        firstTerm = ((1 - (10 * h)) / (1 + (10 * h))) * yi
        secondTerm = ((10 * h) / (1 + (10 * h))) * (math.sin(ti) + math.sin(ti_1))
        thirdTerm = (h / (2 * (1 + (10 * h)))) * (math.cos(ti) + math.cos(ti_1))

        yi_1 = firstTerm + secondTerm + thirdTerm

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
trapezoidal(f, 0, 1, 20, .1)

plt.show()