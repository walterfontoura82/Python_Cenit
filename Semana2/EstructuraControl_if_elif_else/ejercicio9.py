# 9-Escribir un programa que pida al usuario tres números y muestre por pantalla
# el mayor de ellos.


numero1=0
numero2=0
numero3=0

numero1=int(input("Ingrese el primer nuemro: "))
numero2=int(input("Ingrese el segundo nuemro: "))
numero3=int(input("Ingrese el tercer nuemro: "))

if numero1 > numero2 and numero1 > numero3:
    print("El numero mayor es: ",numero1)
elif numero2 > numero1  and numero2 >numero3:
    print("El numero mayor es ", numero2)
else:
    print("El numero mayor es: ", numero3)