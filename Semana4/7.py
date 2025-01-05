'''
7-Crea una función llamada imprimir_pares que tome un número entero como
parámetro y imprima todos los números pares desde 1 hasta ese número.

'''

def imprimir_pares(par):
    for x in range (1, par +1):
        if x % 2 == 0:
            print(x)


#Main
num = int(input("Ingrese un nuemro: "))
imprimir_pares(num)