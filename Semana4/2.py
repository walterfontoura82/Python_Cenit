'''
2-Crea una función llamada saludo que tome el nombre de una persona como
parámetro e imprima un saludo personalizado.

'''

def saludo(nombre):
    return f'Hola {nombre}, como estas? espero que este \n bien \n'

#main
nombre = input("Ingrese si nombre: ")
res = saludo(nombre)
print(res)