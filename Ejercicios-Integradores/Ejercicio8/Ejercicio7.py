#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
#persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
#opcional. Crear los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
#directamente, sólo ingresando o retirando dinero.
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
#negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

from Ejercicio6 import Persona

class Cuenta(Persona):
    
    def __init__(self, pNombre, pEdad, pDni, pCantidad):
        super().__init__(pNombre, pEdad, pDni)
        self.__cantidad = pCantidad
    
    @property
    def cantidad(self):
        return self.__cantidad 
    
    @cantidad.setter
    def set_cantidad(self, pNuevaCantidad):
        self.__cantidad = pNuevaCantidad
        
        
    def mostrar(self):
        return super().mostrar() + " - Dinero: " + str(self.cantidad)
    
    def ingresar(self, cantidad):
        if cantidad >= 0:
            self.__cantidad += cantidad
            
    def retirar(self, cantidad):
        self.__cantidad -= cantidad