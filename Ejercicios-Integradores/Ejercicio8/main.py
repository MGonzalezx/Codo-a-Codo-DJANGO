from Ejercicio6 import Persona
from Ejercicio7 import Cuenta
from Ejercicio8 import CuentaJoven


# Bloque Ppal
def __main__():  #Este método es el método principal donde programo mi programa principal
    p1 = Persona("Juan",22,"45789614")
    print(p1.mostrar())
    '''
    p1.set_nombre = p1.input_nombre()
    p1.set_edad = p1.input_edad()
    p1.set_dni = p1.input_dni()
    print("_____________________________")
    p1.mostrar()
    print(p1.es_mayor_de_edad())
    '''
    print("_____________________________")
    c1 = Cuenta(p1.nombre,p1.edad,p1.dni,500)
    print(c1.mostrar())
    print("_____________________________")
    c1.ingresar(-100)
    c1.ingresar(100)
    print(c1.mostrar())
    print("_____________________________")
    c1.retirar(100)
    print(c1.mostrar())
    print("_____________________________")
    c1.retirar(600)
    print(c1.mostrar())
    print("_____________________________")
    cj1 = CuentaJoven(p1.nombre,p1.edad,p1.dni,500,25)
    print(cj1.mostrar())
    print("_____________________________")
    print(cj1.es_titular_valido())
    print("_____________________________")
    cj1.retirar(50)
    print("_____________________________")
    print(cj1.mostrar())
    
if __name__ == "__main__": #En este caso compruebo que tengo el método main
    __main__() #Si está llamo al método
               #Si no es así estoy ejecutando el main desde otro módulo


