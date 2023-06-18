# 5-Crear un set/conjunto con los números del 1 al 10 y mostrar el número más
# grande en el conjunto.

my_set={1,2,3,4,5,6,7,8,9,10}

print(my_set)

print("##############################")
my_set.add(112)

print(my_set)

print("El mas grande es: ", max(my_set))

print("##############################")

conjunto=set(range(1,30))
mas_grande=max(conjunto)

print("El num mas gramde es: ",mas_grande)