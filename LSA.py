import math
import numpy as np
print()
def l_2(v):
    ret = 0
    for vi in v:
        ret += abs(vi)**2
    return(math.sqrt(ret))

def LSA(x, y, basis):
    A = []
    for i in range(len(x)):
        A.append([])
        for phi in basis:
            A[i].append(phi(x[i]))
    
    A = np.array(A)
    AT = np.matrix.transpose(A)
    ATA = np.dot(AT, A)
    ATy = np.dot(AT, y)

    c = np.linalg.solve(ATA, ATy)
    print("The coefficients c are:")
    print(c)
    RMS_res = l_2(y - np.dot(A, c)) / math.sqrt(6)
    print("The RMS residual is:")
    print(str(RMS_res) + "\n")
    return(RMS_res)

x = [0, .1, .2, .3, .4, .5]
y = [2, 2.20254, 2.40715, 2.61592, 2.83096, 3.05448]
y = np.array(y)

def phi1(x):
    return(1)

def phi2(x):
    return(x)

basis = [phi1, phi2]

print("For the basis {1, x},")
RMS_res_1 = LSA(x, y, basis)

def phi1(x):
    return(1)

def phi2(x):
    return(math.e**x)

def phi3(x):
    return(math.e**(-x))

basis = [phi1, phi2, phi3]

print("For the basis {1, e^x, e^-x},")
RMS_res_2 = LSA(x, y, basis)

print("And so the difference is " + str(abs(RMS_res_1 - RMS_res_2)))