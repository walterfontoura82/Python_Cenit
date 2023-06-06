# 3-Escribir un programa que pida al usuario dos números y muestre por pantalla
# cuál de ellos es mayor.

numero1=0
numero2=0

numero1= float(input("Ingrese el primer numero"))
numero2= float(input("Ingrese el segundo numero"))

if numero1 > numero2:
    print("El numero mayor es: ", numero1)
else:
    print("El numero mayor es: ", numero2)
