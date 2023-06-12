# 7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
# es una letra mayúscula, una letra minúscula, un número o un carácter especial.

caracter=" "




caracter = input("Introduce un carácter: ")

if caracter.isupper():
    print("Es una letra mayúscula.")
elif caracter.islower():
    print("Es una letra minúscula.")
elif caracter.isdigit():
    print("Es un número.")
else:
    print("Es un carácter especial.")

