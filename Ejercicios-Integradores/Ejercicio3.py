#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
#cada palabra que contiene y la cantidad de veces que aparece (frecuencia).


def diccionario(cadena):
  mi_lista= cadena.split() #The split() method splits a string into a list. 
                           #You can specify the separator, default separator is any whitespace
  mi_diccionario={}
  for i in mi_lista: # i sería el string (clave) creado por el split
    if i in mi_diccionario: # si el string esta en el diccionario
      mi_diccionario[i] +=1 #el valor de la clave aumenta por uno
    else:
      mi_diccionario[i]= 1 # en este caso, el string no está en la lista, 
                           #por lo tanto es la primera vez que aparece. Procedemos a darle un valor de 1
  return mi_diccionario


cadena=input('Ingrese su cadena de caracteres: ')
print(diccionario(cadena))
