'''
8-Crea una función llamada es_palindromo que tome una cadena de texto como
parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual
de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso
contrario.
'''
def es_aplindromo(text):
    text = str.lower(text) 
    cadena = text[::-1]
    if cadena == text:
        print("Es palindromo")
    else:
        print("No es palindromo")

#Main
text = input("Ingrese un texto: ")
es_aplindromo(text)