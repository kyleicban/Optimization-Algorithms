import math

def bisection(f, a, b, err):
    if(f(a) * f(b) > 0):
        print("Invalid range")
        return None

    a_n = a
    b_n = b
    p_n = 0
    it = 0

    while(b_n - a_n >= err):
        it += 1
        print("Iteration: " + str(it))
        p_n = (a_n + b_n) / 2
        print("a_" + str(it) + " = " + str(a_n))
        print("p_" + str(it) + " = " + str(p_n))
        print("b_" + str(it) + " = " + str(b_n))
        print("f(a_" + str(it) + ") = " + str(f(a_n)))
        print("f(p_" + str(it) + ") = " + str(f(p_n)))
        print("f(b_" + str(it) + ") = " + str(f(b_n)) + "\n")
        if(f(p_n) == 0):
            return("Found the exact root after " + 
                str(it) + " iterations: " + str(p_n))
        if(f(a_n) * f(p_n) < 0):
            b_n = p_n
        else:
            a_n = p_n
    return("The approximation after " +
        str(it) + " iterations is: " + str(p_n))
    
def func(x):
    return(x**2 - 3)

print(bisection(func, 1, 2, 10**(-4)))
