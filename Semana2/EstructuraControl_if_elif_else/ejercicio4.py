# 4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
# pantalla si está aprobado (5 o más) o no.

#La toma de datos notiene control de ingreso, osea si ingresa una nota 11 igual lo toma

nota=0

sigue="s"

while sigue != "n" : # Genera un bucle por si quieren contral otra nota



    nota= float(input("Ingrese una nota a evaluar: "))
    if nota>=0 and nota <=10:    # Valida que el numero de nota ingresada sea valida
        if nota>=5:
            print("Aprobado")
        else:
            print("NO Aprobado")
        
    else:
        print("numero no valido como nota")
    sigue=input("Desea cargar otra nota: ")
    