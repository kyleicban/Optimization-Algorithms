import math
from matplotlib import pyplot as plt
import numpy as np

def calc_exact():
    def exact(x):
        return(((1/6)*(x**3)*(math.e**x)) - ((5/3)*x*(math.e**x)) + (2*math.e**x) - x - 2)
    
    x = []
    y = []
    x0 = 0
    for i in range(2000):
        x.append(x0)
        y.append(exact(x0))
        x0 += 0.001

    plt.scatter(x, y)

def finiteDifference(p, q, f, x0, ya, yb, h, N):
    A1 = []
    A2 = []
    I = []
    b = []

    xi = x0 + h

    N = N - 1

    x = [x0, xi]
    y = [ya]

    for i in range(N):
        A1.append([])
        A2.append([])
        I.append([])
        for j in range(N):
            if(j == i - 1):
                A1[i].append(1)
                A2[i].append(-1)
                I[i].append(0)
            elif(j == i):
                A1[i].append(-2)
                A2[i].append(0)
                I[i].append(1)
            elif(j == i + 1):
                A1[i].append(1)
                A2[i].append(1)
                I[i].append(0)
            else:
                A1[i].append(0)
                A2[i].append(0)
                I[i].append(0)
        if(i == 0):
            b.append(f(xi) - (ya/(h**2)) + (p* (ya/(2*h))))
        elif(i == N - 1):
            b.append(f(xi) - (yb/(h**2)) - (p* (yb/(2*h))))
        else:
            b.append(f(xi))
        xi = xi + h
        x.append(xi)

    A1 = np.array(A1)
    A2 = np.array(A2)
    I = np.array(I)
    b = np.array(b)

    A = ((1/h**2)*A1) + ((p/(2*h))*A2) + (q*I)

    yn = np.linalg.solve(A, b)
    y = y + list(yn) + [yb]
    print(x)
    print(y)

    plt.scatter(x, y)

def f(x):
    return((x * math.e**x) - x)


calc_exact()
finiteDifference(-2, 1, f, 0, 0, -4, 0.2, 10)

plt.show()