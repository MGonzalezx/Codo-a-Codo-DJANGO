#Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
#cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
#del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
#ejercicio tanto de manera iterativa como recursiva.

#ITERATIVA

def get_int():
    while True:
        input_usuario = input('Ingrese su valor entero: ')
        try:
            value = int(input_usuario)
        except ValueError:
            print('No es un entero!. Vuelva a intentarlo!')
        else:
            return value


get_int()

'''
#RECURSIVA
def get_int():
    input_usuario = input('Ingrese su valor entero: ')
    try:
        value = int(input_usuario)
    except ValueError:
        print('No es un entero!. Vuelva a intentarlo!')
        return get_int()
    else:
        return value


get_int()'''