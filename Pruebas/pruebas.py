'''
print("Hola Mundo")

pepe = 2
print(type(pepe))
pepe = "2"
print(type(pepe))


#ENCLOSING
def saludo_dos():
    """
    descripcion
    """
    mensaje_dos = 'Hola estoy adentro de saludos_dos'

    def bienvenida():
        print(mensaje_dos)

    bienvenida()


saludo_dos()



c = [1,2,3,4,5,6,7,8,9]

print(c)
print(type(c))

if 1 > 2:
    print("algo")
else:
    print("algo")


if 1>2:

elif:
    



nro = int(input("Ingrese el primer numero: "))
nro2 = int(input("Ingrese el segundo numero: "))

suma = nro + nro2

print(suma)


#REPETITIVAS
cajon_frutas = ["manzana","banana","pera"]
for fruta in cajon_frutas:
    print("La fruta es",fruta)
   
for cont in range(1,10,1): #inicio,fin,salto
    print(cont)
   
 
N = int(input("Ingrese valor maximo del contador: "))
for cont in range(1,N,1):
    print(cont)
  

i = 1

while i<=10:
    print(i)
    i= i+1
print("Fin del programa")


suma = 0 #inicializo mi acumulador

num = int(input("Ingrese su numero: "))

while num !=0: #si ingresamos 0 el bucle termina
    suma+= num
    num= int(input("Ingrese su numero: ")) #volvemos a pedir numero evitar caer en un ciclo infinito
                                           # Si es 0, se termina el ciclo, sino sigue sumando
print("La sumatoria es:",suma)

# *args parámetros indeterminados
def mi_suma(*args):
    resultado = 0
    #itero
    for x in args:
        resultado +=x
    return resultado


print(mi_suma(1,2,3,4))


# **kwargs recibo como parámetro un diccionario

def concatenar(**kwargs):
    resultado=""
    print(kwargs['a'])
    #iteramos sobre los valores del diccionario
    for arg in kwargs.values():
        resultado += arg
    return resultado

#print(concatenar(a="codo!"))
print(concatenar(a="Codo ",b="A ",c="Codo",d="!"))


#TUPLAS son inmutables

#creación
tupla = ('uno','dos','tres')
#empaquetado (zip)
tupla = 'Gonzalez, Martin', (30,10,1997), 78956487
#desempaquetado
nombre, nacimiento, dni = ('Gonzalez, Martin', (30,10,1997),78956487)

tupla2 = [1,2,3],[4,5,6]

lista1, lista2 = tupla

#si puedo modificar lista1 y lista2. Pero no puedo hacer lo siguiente: tupla2[0] = 


#acceso
tupla = 'Gonzalez, Martin', (30,10,1997), 78956487
nombre,nacimiento,dni = tupla
print('Nombre:',nombre,'Nacimiento:',nacimiento,'Dni:',dni)


#DICCIONARIOS CLAVE-VALOR
{} #diccionario vacio
{'Juan':56} #diccionario con un elemento
{'Juan':56, 'Ana':15} #diccionario con dos elementos
'''


