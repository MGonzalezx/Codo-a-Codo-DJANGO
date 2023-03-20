class Vehiculo():
    
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
       return "Color: {} - Ruedas: {}".format(self.color, self.ruedas)
   

#Herencia simple de una única superclase

class Auto(Vehiculo):
    
    def __init__(self, color, ruedas,velocidad): #constructor de la clase auto
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        
    #sobreescritura de _str_
    def __str__(self):
        return super().__str__() + " - Velocidad: " + str(self.velocidad)
    
    
v1 = Vehiculo("Blanco",2)
a1 = Auto("Rojo",4,150)
a2 = Auto("Verde",4,140)
a3 = Auto("Azul",4,70)
a4 = Auto("Negro",4,90)

print(v1)
print(a1)
print(a2)
print(a3)
print(a3)