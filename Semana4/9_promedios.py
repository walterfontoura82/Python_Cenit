'''
9-Crea una función llamada promedio que tome una lista de números como
parámetro y devuelva el promedio de esos números.

'''
lista = [1,2,3,4,5,6,7,8,9,12,13,23,23,24,25,45,67]


def promedio(lis):
    prom = 0
    for i in lis:
        prom = prom +i
    denomi = len(lis)
    return (prom/denomi)

#Main
prome = promedio(lista)
print(f'El promedio de la lista ingresada es: {prome}')