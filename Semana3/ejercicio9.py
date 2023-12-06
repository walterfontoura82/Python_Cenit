# Escribe un programa que pida al usuario un número y luego imprima la
# secuencia de Fibonacci correspondiente a ese número.

num1=0
#Solicta un nuemro al usuario
num1= int(input("Ingrese el numero: "))
secuencia=0

a,b =0,1

print("Secuencia de Fibonacci \n")
for i in range(1,num1+1):
    
    print(a,end=",")
    a,b= b, a+b
print('\n')

''' numero 1
1+1=2
1+2=3
2+3=5
3+5=8
5+8=13
8+13=21
13+21=34
'''