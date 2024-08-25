'''
1-Crea una función llamada suma que tome dos números como parámetros y
devuelva la suma de ellos.

'''

def suma(a,b):
    return a+b
#Main
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
resul= suma(a,b)
print(f'El resultado de la suma de los numeros es: {resul}')