import math
from matplotlib import pyplot as plt

def eulers(f, t0, y0, N, h):
    i = 0
    ti = t0
    yi = y0
    yi_1 = -1

    t = [ti]
    y = [yi]

    # print("Iteration: " + str(i))
    # print("t" + str(i) + " = " + str(ti))
    # print("y" + str(i) + " = " + str(yi))

    while(i < N):
        yi_1 = yi + (h * f(ti, yi))
        yi = yi_1
        ti += h
        i += 1

        # print()
        # print("Iteration: " + str(i))
        # print("t" + str(i) + " = " + str(ti))
        # print("y" + str(i) + " = " + str(yi))

        t.append(ti)
        y.append(yi)

    return(yi)
    plt.scatter(t, y)

def f(t, y):
    return(4 * y * (1 - y))

# eulers(f, 0, 1, 0.1, 0.003125)

# plt.show()

def aitken(f, t0, y0, N, h):
    yh = eulers(f, t0, y0, N, h)
    yh_2 = eulers(f, t0, y0, N * 2, h / 2)
    yh_4 = eulers(f, t0, y0, N * 4, h / 4)

    frac = (yh - yh_2)/(yh_2 - yh_4)

    p = math.log(frac)/math.log(2)
    return(p)

N = 10
h = 0.1
for i in range(4):
    print("h = " + str(h))
    print(aitken(f, 0, 0.1, N, h))
    N = N * 2
    h = h / 2
