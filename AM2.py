import math
from matplotlib import pyplot as plt

# specifically for question 4.3 on HW4

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

def AM2(f, t0, y0, N, h):
    i = 0
    ti_p = t0 # t_i-1, abbreviated to ti_previous
    yi_p = y0 # y_i-1, abbreviated to yi_previous
    ti = t0 + h
    yi = RK4(f, t0, y0, 1, h)
    yi_1 = -1

    t = [ti]
    y = [yi]

    d = 12 + 25 * h
    N = N - 1

    while(i < N):
        ti_1 = ti + h
        
        firstTerm = ((25 * h) / d) * (ti_1**2)
        secondTerm = ((10 * h) / d) * ti_1
        thirdTerm = ((12 - (40 * h)) / d) * yi
        fourthTerm = ((40 * h) / d) * (ti**2)
        fifthTerm = ((16 * h) / d) * ti
        sixthTerm = ((5 * h) / d) * (yi_p)
        seventhTerm = ((-5 * h) / d) * (ti_p**2)
        eighthTerm = ((-2 * h) / d) * ti_p
        
        yi_1 = firstTerm + secondTerm + thirdTerm + fourthTerm + fifthTerm + sixthTerm + seventhTerm + eighthTerm
        ti_p = ti
        yi_p = yi
        ti = ti_1
        yi = yi_1
        i += 1

        t.append(ti)
        y.append(yi)

    plt.scatter(t, y)

def f(t, y):
    return(-5 * y + 5 * t**2 + 2 * t)

calc_exact()
AM2(f, 0, 1/3, 10, .1)

plt.show()