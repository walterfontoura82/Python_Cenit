# Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con todas las vocales en mayúscula.

cadena_texto=input("ingrese una cadena de texto: ")
cadena_texto=cadena_texto.replace("a","A").replace("e","E").replace("i","I").replace("o","O").replace("u","U")
print(cadena_texto)