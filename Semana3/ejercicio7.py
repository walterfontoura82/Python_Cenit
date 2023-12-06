# Escribe un programa que pida al usuario una palabra y determine si es un
# palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
# izquierda).

print("Verificaremos si una palabra es un palindromo\n")
print('\n')
palabra= input("ingrese la palabra: ")
palabra_invertida= palabra[::-1]
if palabra == palabra_invertida:
    print("Es un polindromo")
else:
    print("NO Es un polindromo")
