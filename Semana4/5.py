'''
5-Crea una función llamada es_divisible que tome dos números enteros como
parámetros y devuelva Es divisible si el primer número es divisible por el
segundo número, o No es divisible en caso contrario.

'''
def es_divisible(a,b):
    if a % b ==0:
        return ("Es divisible")
    else:
        return("No es divisible")
    
#Main
a = int(input("Ingrese un numerador: "))
b = int (input("Ingrese el divisor: "))
res = es_divisible(a,b)
print(res)