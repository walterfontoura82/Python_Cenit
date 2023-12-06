

            # c=0
            # while c< 5:
            #     c+=1
            #     print(c)
            # else:
            #     print("Se ha completado toda la iteracion y c vale", c)
            # print("\n")
            # print("\n")

            # print ("########## Separadaror   ####################################################")
            # print("Comienzo")
            # for i in range(5):
            #     print("Hola ", end="")
            # print("\nFunal")

            # print ("########## Separadaror   ####################################################")

            # print("\n")
            # print("\n")

            # #Controlar Fin de  Bucle con Brak
            # while True:
            #     op = input("Ingrese cualquier palabra, termina con fin -->")
            #     if op == "fin":
            #         break
            #     else:
            #         print("La palabra ingresada el ", op)
                
            # print("Termino el bucle con fin")


            # #Sentencia continue

            # var=10
            # while var > 0:
            #     var =var -1
            #     if var == 7:
            #         continue
            #     print("Valor actual de var es: ", var)


#   Ejercicios - Estructuras de Control de Loops
# 2-Escribe un programa que pida al usuario un número y calcule la suma de todos
# los números naturales del 1 hasta ese número.

numero= int(input("Ingrese un numero entero= "))
suma=0

for i in range(1,numero+1):
    print("El valor de i es: i", i)
    suma=suma +i
    print("La suma es: ", suma)
print('\n')
print("La suma total es: ", suma)


# # # # Solicitar al usuario un número
# # # numero = int(input("Ingrese un número entero positivo: "))

# # # # Verificar si el número ingresado es positivo
# # # if numero < 1:
# # #     print("Por favor, ingrese un número entero positivo.")
# # # else:
# # #     # Calcular la suma de los números naturales hasta el número ingresado
# # #     suma = 0
# # #     for i in range(1, numero + 1):
# # #         print("i es: ",i)
# # #         suma += i

# # #     # Mostrar el resultado
# # #     print(f"La suma de los números naturales hasta {numero} es: {suma}")
