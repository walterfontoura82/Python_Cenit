# 5-Crea un programa que pida al usuario dos números enteros y muestre en
# pantalla su cociente y su resto.

numero1=0
numero2=0
resto=0
cociente=0

numero1=int(input("ingrese el primer nuemro"))
numero2=int(input("Ingrese el segundo nuemro"))

cociente= numero1 // numero2
resto = numero1 % numero2

print("El cociente de los nuemros es: ",cociente)
print ("El resto de de los nuemros es: ",resto)