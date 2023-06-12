# 10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
# una vocal o una consonante.


letra=" "

letra=input("Ingrese una letra: ")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Es una vocal")
else:
    print("No es una vocal")