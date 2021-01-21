import math

def heuns(f, t0, y0, N, h):
    i = 0
    ti = t0
    yi = y0
    yi_1 = -1

    # print("Iteration: " + str(i))
    # print("t" + str(i) + " = " + str(ti))
    # print("y" + str(i) + " = " + str(yi))

    while(i < N):
        S1 = f(ti, yi)
        S2 = f(ti + h, yi + (h * S1))

        yi_1 = yi + ((h / 2) * (S1 + S2))
        yi = yi_1
        ti += h
        i += 1

        # print()
        # print("Iteration: " + str(i))
        # print("t" + str(i) + " = " + str(ti))
        # print("y" + str(i) + " = " + str(yi))

    return(yi)

# def f(t, y):
#     return(-5 * y + 5 * t**2 + 2 * t)

def f(t, y):
    return(4 * y * (1 - y))

# print(heuns(f, 0, 0.1, 10, 0.1))

def aitken(f, t0, y0, N, h):
    yh = heuns(f, t0, y0, N, h)
    yh_2 = heuns(f, t0, y0, N * 2, h / 2)
    yh_4 = heuns(f, t0, y0, N * 4, h / 4)

    frac = (yh - yh_2)/(yh_2 - yh_4)

    p = math.log(frac)/math.log(2)
    return(p)

# print(aitken(f, 0, 0.1, 10, 0.1))
N = 10
h = 0.1
for i in range(4):
    print("h = " + str(h))
    print(aitken(f, 0, 0.1, N, h))
    N = N * 2
    h = h / 2