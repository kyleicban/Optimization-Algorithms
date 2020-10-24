import math

def newtons(f, f_1, p_0, tol, max_it):
    it = 1
    while(it <= max_it):
        print("Iteration: " + str(it))
        print("f(p_" + str(it-1) + ") = " + str(f(p_0)))
        print("f'(p_" + str(it-1) + ") = " + str(f_1(p_0)))
        p = p_0 - f(p_0)/f_1(p_0)
        print("p_" + str(it) + " = " + str(p))
        if(abs(p - p_0) < tol):
            return("Procedure successful after " + 
                str(it) + " iterations: p = " + str(p))
        it = it + 1
        p_0 = p
    
    return("Procedure unsuccessful: p = " + str(p))

def newtons_modified(f, f_1, f_2, p_0, tol, max_it):
    it = 1
    while(it <= max_it):
        print("Iteration: " + str(it))
        print("f(p_" + str(it-1) + ") = " + str(f(p_0)))
        print("f'(p_" + str(it-1) + ") = " + str(f_1(p_0)))
        print("f''(p_" + str(it-1) + ") = " + str(f_2(p_0)))
        p = p_0 - ( f(p_0)*f_1(p_0) ) / ( (f_1(p_0)**2) - (f(p_0)*f_2(p_0)) )
        print("p_" + str(it) + " = " + str(p))
        if(abs(p - p_0) < tol):
            return("Procedure successful after " + 
                str(it) + " iterations: p = " + str(p))
        it = it + 1
        p_0 = p
    
    return("Procedure unsuccessful: p = " + str(p))

def f(x):
    return(x**3 - (3*x**2)*(2**(-x)) + 3*x*(4**(-x)) - 8**(-x))

def f_1(x):
    return((math.log(8)*(8**-x)) - (3*math.log(4)*x*(4**-x)) + 3*(4**-x) + 3*math.log(2)*(x**2)*(2**-x) - 3*x*(2**(1-x)) + 3*(x**2))

def f_2(x):
    return(-((math.log(8)**2)*(8**-x)) + (3*(math.log(4)**2)*x*(4**-x)) - 6*math.log(4)*(4**-x) - 3*(math.log(2)**2)*(x**2)*(2**-x) + 3*math.log(2)*x*(2**(2-x)) - 3*(2**(1-x)) + 6*x)

print(newtons(f, f_1, 0.5, 10**(-5), 50))
print("")
print(newtons_modified(f, f_1, f_2, 0.5, 10**(-5), 50))