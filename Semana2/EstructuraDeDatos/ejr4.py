# 4-Crear un diccionario con los nombres de tres personas y sus respectivas
# edades. Mostrar la edad de la tercera persona en el diccionario.

"""
#Se cargan los registros desde el principio
print("###################################################")
nombre_personas={"Walter":41,"Rene":70,"cyn":43}
print(nombre_personas)

"""


#Creamos el diccionario solicitando primero los tres nombres y luego que carguen las edades.

nombre_personas={}

for i in range(4):
    nombre=input("ingrese el nombre a cargar: ")
    nombre_personas[nombre]=0

# Recorre los nombres cargados, muestra el nombre y solcita que cargues la edad correspondiente
for nombre in nombre_personas:
    edad = int(input("Ingresa la edad de {}:".format(nombre)))
    nombre_personas[nombre]=edad

#imprimier el registro

print("\nRegistro de frutas y precios:")
for nombre, edad in nombre_personas.items():
    print("La Edad de {} es {:}".format(nombre, edad))
