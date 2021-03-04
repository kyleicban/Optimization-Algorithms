import math
import numpy as np
from matplotlib import pyplot as plt

def calc_exact(h, N):
    def exact(x):
        return(((1/6)*(x**3)*(math.e**x)) - ((5/3)*x*(math.e**x)) + (2*math.e**x) - x - 2)
    
    y = []
    x0 = 0
    for i in range(N + 1):
        y.append(exact(x0))
        x0 += h

    return(np.array(y))

def finiteDifference(p, q, f, x0, ya, yb, h, N):
    A1 = []
    A2 = []
    I = []
    b = []

    xi = x0 + h

    N = N - 1

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

    A1 = np.array(A1)
    A2 = np.array(A2)
    I = np.array(I)
    b = np.array(b)

    A = ((1/h**2)*A1) + ((p/(2*h))*A2) + (q*I)

    yn = np.linalg.solve(A, b)
    y = y + list(yn) + [yb]

    return(np.array(y))

def f(x):
    return((x * math.e**x) - x)

def l_1(v):
    ret = 0
    for vi in v:
        ret += abs(vi)
    return(ret)

def l_2(v):
    ret = 0
    for vi in v:
        ret += abs(vi)**2
    return(math.sqrt(ret))

def l_inf(v):
    ret = 0
    for vi in v:
        if abs(vi) > ret:
            ret = abs(vi)
    return(ret)

y_exact_02 = calc_exact(0.2, 10)
y_02 = finiteDifference(-2, 1, f, 0, 0, -4, 0.2, 10)
print(y_02)

y_exact_01= calc_exact(0.1, 20)
y_01 = finiteDifference(-2, 1, f, 0, 0, -4, 0.1, 20)
print(y_01)

y_exact_005 = calc_exact(0.05, 40)
y_005 = finiteDifference(-2, 1, f, 0, 0, -4, 0.05, 40)
print(y_005)

e_02 = y_exact_02 - y_02
e_02 = list(e_02)

e_01 = y_exact_01 - y_01
e_01 = list(e_01)

e_005 = y_exact_005 - y_005
e_005 = list(e_005)

h = [0.2, 0.1, 0.05]

e_1 = [l_1(e_02), l_1(e_01), l_1(e_005)]
e_2 = [l_2(e_02), l_2(e_01), l_2(e_005)]
e_inf = [l_inf(e_02), l_inf(e_01), l_inf(e_005)]

plt.scatter(h, e_1)
plt.scatter(h, e_2)
plt.scatter(h, e_inf)

plt.show()