import math
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 10 * math.sin(x)


a = 2
b = 3
e = 10**-6
iterations = []
x_values = []

x = a - f(a) * (b - a) / (f(b) - f(a))
x_values.append(x)

solution_found = False
for i in range(1, 10):
    x_old = x
    x = a - f(a) * (b - a) / (f(b) - f(a))
    x_values.append(x)
    zn = x - x_old
    iterations.append((a, b, x))
    print(f"Ітерація {i}: x = {x:.10f}, f(x) = {f(x):.10f}, Точність: {abs(zn):.10f}")
    if f(a) * f(x) < 0:
        b = x
    else:
        a = x
    if abs(f(x)) < e:
        if not solution_found:
            print(f"Досягнуто необхідної точності на ітерації {i}, розв'язок з заданою точністю {e}: {x:.10f}")
            solution_found = True


x_min = 2.4
x_max = 2.6
x_graph = [x_min + i * (x_max - x_min) / 400 for i in range(401)]
y_graph = [f(xi) for xi in x_graph]

plt.figure(figsize=(10, 6))
plt.plot(x_graph, y_graph, label='f(x)')
plt.axhline(0, color='black', linewidth=0.5)


for idx, (a_i, b_i, x_i) in enumerate(iterations):
    plt.plot([a_i, b_i], [f(a_i), f(b_i)], 'g--', linewidth=1)
    plt.plot(x_i, 0, 'ro')

    plt.text(x_i, 0, f'  x{idx+1}', verticalalignment='bottom')


plt.xlim(x_min, x_max)
plt.ylim(min(y_graph), max(y_graph))

plt.title('Метод хорд')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
