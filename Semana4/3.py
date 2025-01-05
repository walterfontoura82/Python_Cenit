'''
3-Crea una función llamada invertir_cadena que tome una cadena de texto como
parámetro y devuelva la cadena invertida.

'''
def invertir_cadena(cadena):
    return cadena[::-1]

cadena = input("ingrese un texto: ")
result = invertir_cadena(cadena)
print(result)
        