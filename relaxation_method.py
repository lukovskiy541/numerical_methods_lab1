import math
x = 3.0
e = 10**-6
t = 0.083
M1 = 15.89
m1 = 8.16
q = (M1 - m1) / (M1 + m1)

def f_der(x):
    return 2*x - 10 * math.cos(x)

def f(x):
    return x**2 - 10 * math.sin(x)


solution_found = False
for i in range(1, 10):
    xn = x - t * f(x)
    convergence = 'Збігається' if (0 < t * f_der(xn) < 2) else 'не збігається'
    zn = xn - x
    print(f"Ітерація {i}: x = {x:.10f}, f(x) = {f(x):.10f}, Збіжність: {convergence}, Точність: {zn:.10f}")
    
    if abs(zn) < e:
        if not solution_found: 
            print(f"Досягнуто необхідної точності на ітерації {i}, розв'язок з заданою точністю {e}:  {x:.10f}")
            solution_found = True

    x = xn
