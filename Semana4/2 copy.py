'''
2-Crea una función llamada saludo que tome el nombre de una persona como
parámetro e imprima un saludo personalizado.
'''
def saludo(nombre):
    print(f'Que tengas un excelente dia {nombre}')

# Main
nombre = input("Ingrese un nombre: ")
saludo(nombre)