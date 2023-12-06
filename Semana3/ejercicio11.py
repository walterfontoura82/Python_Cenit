# 11-Escribe un programa que pida al usuario un número y calcule su factorial.
# Un factorial es el producto que resulta de multiplicar un número entero positivo
# dado por todos los enteros inferiores a él hasta el uno. Por ejemplo, el factorial
# de 4 es 4! = 4 × 3 × 2 × 1 = 24


def calcualr_factorial(numero):
    if numero < 0:
        return "El nuemro no esta definido para numeros negativos"
    elif numero == 0 or numero == 1 :
        return 1
    else :
        factorial = 1
        for i in  range(2, numero + 1):
            factorial *= i
        return factorial
    

    #Solcit el num al usuario

numero_usuario= int(input("Ingrese el numero factorial"))

resultado_factorial= calcualr_factorial(numero_usuario)
print(f"El factorial de {numero_usuario} es: {resultado_factorial}")
