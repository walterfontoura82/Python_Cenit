# 11-Escribir un programa que pida al usuario dos números y muestre por pantalla
# la suma de ellos solo si ambos son pares.


numero1= 0
numero2= 0

numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))


if numero1 %2 == 0 and numero2 %2 == 0 :
    print("La suma d elos numero pares es: ", numero2 + numero1)
else:
    print("Al menos uno de los dos numeros es impar")