# Escribe un programa que pida al usuario una palabra y luego imprima la misma
# palabra pero con las letras en orden inverso.

    # palabra= input("Ingrese una palabra: \n")
    # print(palabra)
    # for i in palabra:
    #     print(i)

# Solicitar al usuario una palabra
palabra = input("Ingrese una palabra: ")
print(len(palabra))

# Invertir la palabra
palabra_invertida = palabra[::-1]

# Imprimir la palabra invertida
print(f"La palabra invertida es: {palabra_invertida}")
