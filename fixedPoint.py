import math

def fixedPoint(g, p_0, tol, it_max):
    it = 1
    p = -1

    while(it <= it_max):
        print("Iteration: " + str(it))
        p = g(p_0)
        print("g(" + str(p_0) + ") = " + str(g(p_0)))
        if(abs(p - p_0) < tol):
            return("Procedure successful after " + 
                str(it) + " iterations: p = " + str(p))
        it += 1
        p_0 = p

    return("Procedure unsuccessful: p = " + str(p))
    
def g(x):
    return((3*x)**(1/3))

print(fixedPoint(g, 1, 10**(-4), 10))