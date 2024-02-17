import math

def calcular_funcion(x):
    sin_2x_cuadrado = math.sin(2 * x**2)
    valor_absoluto_x = abs(x)
    resultado = 3 + x * math.pi + sin_2x_cuadrado / (2 * valor_absoluto_x)

    return resultado


print("Ingresa el valor de x estupido")
x = int(input())
resultado = calcular_funcion(x)
print("El resultado de x es", x, "es:", resultado, " ponte a estuiar cabron")
