# 4-Crea una función llamada es_capicua que tome un número como parámetro y
# devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
# derecha a izquierda) y False en caso contrario.

def es_capicua(text):
    if text == text[::-1]:
        print("Es capicua")
    else:
        print("No es capicua")
        
#Main
palabra = input("Ingrese palabra para anlaizar: ")
es_capicua(palabra)
    