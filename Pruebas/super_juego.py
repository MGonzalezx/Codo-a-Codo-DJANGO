from importlib.util import set_loader
import random

class Dado:
    # _valor el _ es un "pacto" de desarrolladores para decir que la variable es privada
    
    def __init__(self):
        self.__valor = 1
        
    def tirar(self):
        self.__valor = random.randint(1,6)
        
    def imprimir(self):
        print(f"Salió: {self.__valor}")
    
    def obtener_valor(self):
        return self.__valor
    
    @property
    def valor(self):
        return self.__valor 
    
    @valor.setter
    def valor(self, pNuevoValor):
        self.__valor = pNuevoValor

class JuegoDado:
    
    def __init__(self):
        self.dado_1 = Dado()
        self.dado_2 = Dado()
        self.dado_3 = Dado()
        
    #Metodo auxiliar
    def __tirardados(self):
        self.dado_1.tirar() 
        self.dado_2.tirar() 
        self.dado_3.tirar() 
         
    def jugar(self):
        self.__tirardados()  
        #self.dado_1.valor = 12  
        self.dado_1.imprimir()
        #self.dado_2.tirar()    
        self.dado_2.imprimir()
        #self.dado_3.tirar()    
        self.dado_3.imprimir()
        
       
        
        if self.dado_1.obtener_valor() == self.dado_2.obtener_valor() == self.dado_3.obtener_valor():
            print("Ganaste!!")
        else:
             print("Perdiste :(")
    
           
             
mi_juego = JuegoDado()
mi_juego.jugar()