import math
print("Ingresa el valor de x:")
base_x=int(input("> "))
base_x=(3+(base_x*math.pi)+math.sin((2*(base_x**2))))/(2*(math.fabs(base_x)))
print("El valor de su funcion de acuerdo a el dato ingresado es:",base_x)
