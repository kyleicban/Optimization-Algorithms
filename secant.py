import math

def secant(f, p_0, p_1, tol, it_max):
    it = 2
    q_0 = f(p_0)
    q_1 = f(p_1)

    while(it - 1 < it_max):
        print("Iteration: " + str(it - 1))
        print("q_" + str(it-2) + " = " + str(f(p_0)))
        print("q_" + str(it-1) + " = " + str(f(p_1)))
        p = p_1 - q_1*(p_1 - p_0)/(q_1 - q_0)
        print("p_" + str(it-2) + " = " + str(p_0))
        print("p_" + str(it-1) + " = " + str(p_1))
        print("p_" + str(it) + " = " + str(p))
        if(abs(p - p_1) < tol):
            return("Procedure successful after " + 
                str(it) + " iterations: p = " + str(p))
        it = it + 1
        p_0 = p_1
        q_0 = q_1
        p_1 = p
        q_1 = f(p)

    return("Procedure unsuccessful: p = " + str(p))

def f(x):
    return((math.e)**x + 2**(-x) + 2*math.cos(x) - 6)

print(secant(f, 1, 2, 10**(-5), 20))