# 5-Escribir un programa que pida al usuario un número entero y muestre por
# pantalla si es par o impar.

numero=0

numero = int(input("Ingrese un nuemro entero: "))

if numero % 2 != 0 :
    print("El numero ingresado es impar")
else:
    print("El numero es par")