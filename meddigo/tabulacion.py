import base64
print("Ingresa tu texto:")
texto_ingresado=input("> ")
codificado=texto_ingresado.encode()
print("Que deseas hacer:")
print("1-pasar texto a base 64")
print("2-pasar a 16 a base 16")
opcion=int(input("> "))
if opcion == 1: 
    codificado=base64.standard_b64encode(codificado)
elif opcion == 2:
    codificado=base64.b16encode(codificado)
print(codificado)
