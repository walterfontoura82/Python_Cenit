# 1-Crear un diccionario con los nombres de tres frutas y sus respectivos precios y
# mostrar el diccionario completo.


registro_frutas = {}

# Ingresar las frutas
for i in range(6):
    fruta = input("Ingresa el nombre de la fruta: ")
    registro_frutas[fruta] = 0

# Ingresar los precios de cada fruta
for fruta in registro_frutas:
    precio = float(input("Ingresa el precio de {}:".format(fruta)))
    registro_frutas[fruta] = precio

# Imprimir el registro completo
print("\nRegistro de frutas y precios:")
for fruta, precio in registro_frutas.items():
    print("{}: ${:.2f}".format(fruta, precio))
