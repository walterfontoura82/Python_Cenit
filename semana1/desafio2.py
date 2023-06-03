# Desafío 2:
# Escribe un programa que solicite al usuario su información personal, incluyendo
# su nombre completo, edad, estatura, peso, dirección y número de teléfono.
# A continuación, el programa deberá imprimir un mensaje con los datos
# ingresados por el usuario en el siguiente formato:

        # La información ingresada es la siguiente:
        # Nombre completo: [nombre completo]
        # Edad: [edad]
        # Estatura: [estatura] cm
        # Peso: [peso] kg
        # Dirección: [dirección]
        # Número de teléfono: [número de teléfono]

# Debemos guardar en un registro  --> usuario{ Nombre_completo, Edad, Estatura, Peso, Direccion, N_Telefeno}

usuario={}
usuario["Nombre_Completo"]=input("Ingrese su nombre: ")
usuario["Edad"]=input("Ingrese su Edad: ")
usuario["Estatura"]=input("Ingrese su Estatura: ")
usuario["Peso"]=input("Ingrese su peso: ")
usuario["Direccion"]=input("Ingrese su Direccion: ")
usuario["N_Telefono"]=input("Ingrese su numero de telefono: ")

print (usuario)
# O imprimimo con formato
print("#####################################################")   #separardor

print("Nombre completo: ",usuario["Nombre_Completo"])
print("Edad: ",usuario["Edad"])
print("Estatura: ",usuario["Estatura"])
print("Peso: ",usuario["Peso"])
print("Direccion: " ,usuario["Direccion"])
print("Telefono: ",usuario["N_Telefono"])
