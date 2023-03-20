#Clases y objetos
#Defino la clase

'''
class Persona:
    nombre = ""
    edad = 15
    
    #Para poder inicializar el objeto voy a necesitar al objeto mismo (self) y un dato más
    #que va a ser el nombre. self es un atributo que permite definir al objeto a si mismo.
    def inicializar(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad
        
        
    def imprimir(self):
        print("Nombre: {}".format(self.nombre)) #Mostramos la informacion del mismo objeto: nombre
        
        
    def cumpleaños(self):
        """
        Cumple años, por lo tanto sube por uno la edad
        """
        edad+=1
        
    def mayor_edad(self):
        if self.edad >=18:
            print("Es mayor edad")
        else:
            print("No es mayor de edad")
            
           
#Programa principal
#Instanciar (crear) el objeto de tipo Persona
persona1= Persona() #Llamamos a la clase y creamos el objeto
persona1.imprimir() # El Nombre está vacío
persona1.inicializar("Juan Pablo", 25) #No es necesario pasar el sefl 
persona1.imprimir() #No tengo que pasarle un parámetro porque Python entiende que debo usar los proios datos del objeto



persona2= Persona() #Es otra persona creada a partir de la misma clase, otra instancia, otro objeto
persona2.inicializar("Carla", 33) #El cambio de estado está asociado a este objeto
persona2.imprimir()

persona3= Persona()
persona3.inicializar("Pedro", 15)
persona3.imprimir()
persona1.mayor_edad()
persona2.mayor_edad()
persona3.mayor_edad()




lista_de_objetos = [persona1, persona2, persona3]        
'''

class Cliente:
    suspendidos=[] # Variables de clase: Los atributos son independientes por cada objeto o instancia de la clase, es decir si definimos tres objetos de la clase Persona, todas las personas tienen un atributo nombre pero cada uno tiene un valor independiente.
                   # En algunas situaciones necesitamos almacenar datos que sean compartidos por todos los objetos de dicha clase, en esas situaciones debemos emplear variables de clase.
                   # Para definir una variable de clase lo hacemos dentro de la clase pero fuera de sus métodos:
                   # https://pythones.net/variables-de-clases/
                   
    def __init__(self,codigo,nombre):
        self.codigo=codigo #Variable de Instancia
        self.nombre=nombre #Variable de Instancia

    def imprimir(self):
        print("Codigo: {}".format(self.codigo))
        print("Nombre: {}".format(self.nombre))
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("No esta suspendido")
        print("_____________________________")

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)

# Bloque principal
cliente1=Cliente(1,"Juan")
cliente2=Cliente(2,"Ana")
cliente3=Cliente(3,"Diego")
cliente4=Cliente(4,"Pedro")

cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()   
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.suspendidos)