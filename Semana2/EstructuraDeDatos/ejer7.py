# 7-Crear un diccionario con los nombres de tres ciudades y sus respectivas
# poblaciones. Agregar una cuarta ciudad al diccionario con su respectiva
# población. Mostrar el diccionario resultante.


# declaramos el diccionarios

ciudades= {}

# Ingresamos los datos de las ciudades al diccionario y sus respectivas poblaciones


for i in range(3):
    ciudad= input(f"Ingrese el nombre de la ciudad")
    poblacion= int(input(f"ingrese la poblacion de {ciudad}: "))
    ciudades[ciudad]= poblacion


#Ingrese los datps de la siguinte ciudad
cuarta_ciudad= input("Ingrese el nombre de la cuearta ciudad: ")
poblacion_cuarta= int (input(f"Ingrse la poblacion de {cuarta_ciudad}: "))
ciudades[cuarta_ciudad]= poblacion_cuarta


#;Mostratr el diccionario resultante
print("Diccionario de Ciudades y sus Poblacion")
for ciudad, poblacion in ciudades.items():
    print(f"{ciudad}: {poblacion}")