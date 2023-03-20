#Escribir una función que calcule el máximo común divisor entre dos números

def maximo_comun_divisor(a, b):
    auxiliar = 0
    while b != 0:
        auxiliar = b
        b = a % b
        a = auxiliar
    return a

a = 20
b = 6

resultado = maximo_comun_divisor(a,b)

print(f"El Máximo común divisor de {a} y {b} es {resultado}.")
