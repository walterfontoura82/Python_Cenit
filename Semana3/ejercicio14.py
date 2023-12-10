#       4-Escribe un programa que pida al usuario un número y luego imprima un
#       triángulo de números como el siguiente:
#       1
#       2 2
#       3 3 3
#       4 4 4 4
#       5 5 5 5 5


numero=int(input("Ingrese un nuemro: "))

for i in range(1,numero+1):
    print(f'{i}' * i)
