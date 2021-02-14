import math

def aitken(f, t0, y0, N, h):
    yh = eulers(f, t0, y0, N, h)                # useless by itself, need to include a method
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

# print("Iteration: " + str(i))
# print("t" + str(i) + " = " + str(ti))
# print("y" + str(i) + " = " + str(yi))

# print()
# print("Iteration: " + str(i))
# print("t" + str(i) + " = " + str(ti))
# print("y" + str(i) + " = " + str(yi))