"""
| Desarrollar un programa que permita cargar n números enteros y luego
nos informe cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional
(este operador retorna el resto de la división de dos valores, por ejemplo
11%2 retorna un 1):
if valor%2==0:
"""


n = int(input("ingrese el limite de numeros enteros : "))
x = 0
par = 0 
impar = 0

while x < n :
    num = int(input("ingrese un numero : "))
    if num % 2 == 0 :
        par = par + 1
    else : 
        impar = impar + 1
    x = x + 1
print(f"la cantidad de numeros pares es de {par}")
print(f"la cantidad de numeros impares es de {impar}")