from abc import ABC, abstractmethod

#Creamos una interfaz, los metodos que va a tener la clase
#Es como una maqueta vacia que otras clases van a utilizar a su manera
class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def emitir_sonido(self):
        print("Animal emite sonido: ", end="")