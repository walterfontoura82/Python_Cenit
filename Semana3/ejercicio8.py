# Escribe un programa que pida al usuario una cadena de texto y luego imprima
# el número de palabras que contiene.

from pprint import pprint

lista_parrafo=[]
parrafo= input("Ingrese un parrafo: \n")
print('\n')
lista_parrafo=parrafo.split()
pprint(lista_parrafo)
print(f'La cantidad de palabras es: {len(lista_parrafo)}')