#Escribe un programa que escriba los 
# numero pares del 1 al 100

        # for i in range(2, 101,2):
        #     print(i) 

for i in range(1,101):
    resto = i % 2
    if resto == 0:
        print(i)