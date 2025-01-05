# 10-Crea una función llamada calcular_factorial que tome un número entero como
# parámetro y devuelva el factorial de ese número. El factorial de un número
# entero positivo n se define como el producto de todos los números enteros
# positivos desde 1 hasta n.


def calcularFactorial(num):
    if num < 0:
        return 'El factorial no esta definido para numeros negativos'
    elif num == 0 or num == 1:
        return 1
    else:
        factorial= 1
        for i in range(2, num +1 ):
            factorial *= i
        return factorial

# Main
num = int(input("Ingrese el num a calcular el factorial: "))
res = calcularFactorial(num)
print(f'El factorial de {num} es: {calcularFactorial(res)}')