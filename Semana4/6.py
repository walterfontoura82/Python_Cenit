'''
6-Crea una función llamada es_par que tome un número como parámetro y
devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
devuelva Es impar o No es par.

'''

def es_par(num):
    if num % 2 ==0:
        return ("Es par")
    else:
        return ("Es impar")
    
#Main
num = int(input("Ingrese un numero: "))
res = es_par(num)
print(res)