from animal import Animal

class Gato(Animal):
    
    def mover(self):
        print("El gato se esta moviendo")
        
    def emitir_sonido(self):
        super().emitir_sonido()
        print("miau, miau")