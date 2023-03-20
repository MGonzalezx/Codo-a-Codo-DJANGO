# Escribir una función que calcule el mínimo común múltiplo entre dos números

#MCM(a, b) = (a * b) / MCD(a, b)

def maximo_comun_divisor(a, b):
    auxiliar = 0
    while b != 0:
        auxiliar = b
        b = a % b
        a = auxiliar
    return a

def minimo_comun_multiplo(a, b):
    return (a * b) / maximo_comun_divisor(a, b)


a = 20
b = 6

resultado = minimo_comun_multiplo(a,b)

print(f"El mínimo común múltiplo de {a} y {b} es {resultado}.")
