'''

3-Crea una función llamada invertir_cadena que tome una cadena de texto como
parámetro y devuelva la cadena invertida.

'''

def invertir_cadena(text):
    pal_inver = text[::-1]
    return pal_inver

#Main
palabra=input("Ingrese la plabra que desea invertir: ")
res = invertir_cadena(palabra)
print(f"La palabra invertida es: {res}")