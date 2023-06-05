# 9-Escribe un programa que solicite al usuario dos números y luego imprima la
# suma, la resta, la multiplicación y la división de los dos números.

numero1=0
numero2=0

numero1=float(input("ingrese el primer numero: "))
numero2=float(input("ingrese el segundo numero: "))

print("La suma de los numeros es: ", numero1 + numero2)
if numero1>numero2:
    print("La resta de los numeros es: ", numero1 - numero2)
else:
    print("La resta de los nemro es: ", numero2 - numero1)

print("La multiplicacion de los nuemros es: ", numero1 * numero2)
if numero1>numero2:
    print("La division de los numeros es: ", numero1 / numero2)
else:
    print("La division de los nemro es: ", numero2 / numero1)