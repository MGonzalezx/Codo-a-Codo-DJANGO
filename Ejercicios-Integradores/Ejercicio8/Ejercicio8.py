#Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
#CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
#además del titular y la cantidad se debe guardar una bonificación que estará expresada en
#tanto por ciento. Crear los siguientes métodos para la clase:
# Un constructor.
# Los setters y getters para el nuevo atributo.
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
#tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
#mayor de edad pero menor de 25 años y falso en caso contrario.
# Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
#cuenta.

from Ejercicio7 import Cuenta


class CuentaJoven(Cuenta):
    def __init__(self, pNombre, pEdad, pDni, pCantidad,pbonificacion):
        super().__init__(pNombre, pEdad, pDni, pCantidad)
        self.__bonificacion = pbonificacion
        
    @property
    def bonificacion(self):
        return self.__cantidad 
    
    @bonificacion.setter
    def set_bonificacion(self, pNuevaBonificacion):
        self.__bonificacion = pNuevaBonificacion
        
    def es_titular_valido(self):
        if self.edad >= 18 and self.edad < 25:
            return True
        else:
            return False
        
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
            print("Dinero retirado!")
        else:
            print("El titular no es válido!")
            
    def mostrar(self):
        return super().mostrar() + " - Bonificacion: " + str(self.__bonificacion) + "%"