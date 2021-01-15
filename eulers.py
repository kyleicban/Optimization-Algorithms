import math
from matplotlib import pyplot as plt

def eulers(f, t0, tn, y0, h):
    i = 0
    ti = t0
    yi = y0
    yi_1 = -1

    t = [ti]
    y = [yi]

    print("Iteration: " + str(i))
    print("t" + str(i) + " = " + str(ti))
    print("y" + str(i) + " = " + str(yi))

    while(ti < tn):
        yi_1 = yi + (h * f(ti, yi))
        yi = yi_1
        ti += h
        i += 1

        print()
        print("Iteration: " + str(i))
        print("t" + str(i) + " = " + str(ti))
        print("y" + str(i) + " = " + str(yi))

        t.append(ti)
        y.append(yi)

    plt.scatter(t, y)

def f(t, y):
    return(-5 * y + 5 * t**2 + 2 * t)

eulers(f, 0, 1, 1/3, 0.1)

plt.show()