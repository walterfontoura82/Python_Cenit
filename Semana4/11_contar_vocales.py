'''
11-Crea una función llamada contar_vocales que tome una cadena de texto como
parámetro y devuelva el número de vocales que contiene.

'''


def contar_vocales(texto):
    # Definir las vocales
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    # Crear un conjunto para almacenar las vocales únicas encontradas
    vocales_encontradas = set()
       
                # 2. Características de set()
                #     set() es un tipo de colección en Python con las siguientes características:

                #     No admite duplicados: Cada elemento solo puede aparecer una vez. Si intentas agregar un elemento ya existente, simplemente se ignora.
                #     Orden no garantizado: Los elementos no se almacenan en un orden predecible.
                #     Acceso eficiente: Las operaciones de búsqueda, inserción y eliminación son rápidas, con una complejidad promedio de tiempo de O(1)
                
    
    # Contar las vocales
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
            vocales_encontradas.add(letra.lower())  # Usamos lower para evitar duplicados de mayúsculas
    
    # Devolver el número total de vocales y las vocales encontradas
    return contador, sorted(vocales_encontradas)

# Ejemplo de uso
texto = input("Ingrese la cadena para buscar vocales")
numero_vocales, vocales_usadas = contar_vocales(texto)
print(f"El número de vocales es: {numero_vocales}")
print(f"Las vocales encontradas son: {', '.join(vocales_usadas)}")

                # Caracteristcas de join:
                #                 Toma la lista vocales_usadas y convierte sus elementos en una cadena de texto, separando cada elemento por la coma y un espacio (, ).
                #                 Si la lista vocales_usadas contiene ['a', 'e', 'o', 'u'], join devolverá la cadena 'a, e, o, u'.
                #                 join es un método que solo se puede aplicar a objetos iterables (como listas o tuplas) y convierte todos los elementos en una cadena de texto con un separador definido.
