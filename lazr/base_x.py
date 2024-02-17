import base64


def texto_a_base64(texto):
    texto_bytes = texto.encode("utf-8")
    base64_bytes = base64.b64encode(texto_bytes)
    base64_texto = base64_bytes.decode("utf-8")
    return base64_texto


def texto_a_base16(texto):
    texto_bytes = texto.encode("utf-8")
    base16_texto = texto_bytes.hex()
    return base16_texto


texto_usuario = input("Ingrese el texto que desea convertir: ")

opcion = input("¿Desea convertir a Base64 o Base16? (Ingrese 64 o 16): ")

if opcion == "64":
    resultado = texto_a_base64(texto_usuario)
    print("Texto en Base64:", resultado)
elif opcion == "16":
    resultado = texto_a_base16(texto_usuario)
    print("Texto en Base16:", resultado)
else:
    print(
        "Opción no válida. Por favor ingrese '64' o '16' para elegir la codificación."
    )
