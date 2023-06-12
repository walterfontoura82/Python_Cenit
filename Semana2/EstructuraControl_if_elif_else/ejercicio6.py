# 6-Escribir un programa que pida al usuario un número entero y muestre por
# pantall2a si es múltiplo de 2 y de 3 a la vez.


numero=0

numero= int(input("Ingrese un numero entero: "))

if numero%2 == 0 and numero % 3 == 0 :
    print("Es multiplo de 2 y de 3")
else:
    print(" No es multiplo de 2 o de 3 a la vez")