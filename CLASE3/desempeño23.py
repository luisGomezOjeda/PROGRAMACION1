# Realizar un programa que permita cargar dos listas de 15 valores
# cada una. Informar con un mensaje cual de las dos listas tiene un valor
# acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas
# iguales")
# Tené en cuenta que puede haber dos o más estructuras repetitivas
# en un algoritmo.


acum1 = 0
acum2 = 0

x = 1

while x <= 15 : 
    lista = int(input(f"ingrese el valor {x} de la lista 1 de 15 valores : "))
    acum1 = acum1 + lista
    x = x + 1
print(acum1)

x = 1
while x <= 15 : 
    lista = int(input(f"ingrese el valor {x} de la lista 2 de 15 valores : "))
    acum2 = acum2 + lista
    x = x + 1

if acum1 > acum2 :
    print("la lista 1 es mayor")
if acum2 > acum1 : 
    print("la lista 2 es mayor")
if acum1 == acum2 :
    print("la lista 1 y la lista 2 acumulan el mismo valor")