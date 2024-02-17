def calcular_funcion(x):
    return 248 * x**2 + 28 * x - 89

print(" x   |   f(x)")
print("--------------")

x = -4.0
while x <= 2.0:
    resultado = calcular_funcion(x)
    print("{:5.2f} | {:7.2f}".format(x, resultado))
    x += 0.25
