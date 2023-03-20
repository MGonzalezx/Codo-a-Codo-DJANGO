from animal import Animal

class Perro(Animal):
    
    def mover(self):
        print("El perro se esta moviendo")
        
    def emitir_sonido(self):
        super().emitir_sonido()
        print("guau, guau")