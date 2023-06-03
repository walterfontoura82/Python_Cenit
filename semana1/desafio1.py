# Desafío 1:
# Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
# sus ventas totales y el departamento comercial te solicita que ayudes a los
# vendedores a calcular sus comisiones creando un programa que les pregunte su
# nombre y cuánto han vendido en éste mes.
# Tu programa le va a responder con una frase que incluya su nombre y el monto
# que le corresponde por las comisiones

#  nombre = string, es el nombre de cada vendedor
#  ventas{clave ,nombre:
#         ventas:     }


nombre=""
ventas=0
comision=0
nombre = input(" Ingrese su nombre")
ventas=float(input("ingrese las ventas del mes: "))
comision= (ventas* 6) / 100
print("las comisiiones de ",nombre + "son de : ", comision )