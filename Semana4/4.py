'''
4-Crea una función llamada es_capicua que tome un número como parámetro y
devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
derecha a izquierda) y False en caso contrario.

'''

def es_capicua(palablra):
    capi = palablra[::-1]
    if capi == palablra :
        print("True")
    else:
        print("False")
        
# Main
palabra = input("Ingrese una palabra: ")
es_capicua(palabra)