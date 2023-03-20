# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
#siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona():
    
    def __init__(self,pNombre,pEdad,pDni):
        self.__nombre = pNombre
        self.__edad = pEdad
        self.__dni = pDni
        
        
    @property
    def nombre(self):
        return self.__nombre 
    
    @nombre.setter
    def set_nombre(self, pNuevoNombre):
        self.__nombre = pNuevoNombre
        
              
    @property
    def edad(self):
        return self.__edad 
    
    @edad.setter
    def set_edad(self, pNuevaEdad):
         self.__edad = pNuevaEdad
            
    
    @property
    def dni(self):
        return self.__dni 
    
    @dni.setter
    def set_dni(self, pNuevoDni):
        self.__dni = pNuevoDni
            
        
    def mostrar(self):
        #print(f"Nombre: {self.__nombre} - Edad: {self.__edad} - DNI: {self.__dni}")
        return "Nombre: {} - Edad: {} - DNI: {}".format(self.nombre, self.__edad,self.__dni)
        
    def es_mayor_de_edad(self):
        if self.__edad >= 18:
            return True
        else:
            return False
    
    
    def input_nombre(self):
        while True:
            input_usuario = input("Ingrese nombre: ")
            try:
                value = str(input_usuario)
                assert (value.isalpha()),"Error de formato, intente devuelta" 
            except AssertionError as error:
                print(error)   
            except:
                print('Error inesperado!')
            else:
                return value  
            
    def input_edad(self):
        while True:
            input_usuario = input("Ingrese edad: ")
            try:
                value = int(input_usuario)
            except ValueError:
                print('No es un entero!. Vuelva a intentarlo!')  
            else:
                return value   
            
    def input_dni(self):
        while True:
            input_usuario = input("Ingrese dni: ")
            try:
                value = str(input_usuario)
                assert (len(value) == 8 ),"El dni tiene que tener 8 numeros" 
            except AssertionError as error:
                print(error)   
            except ValueError:
                print('No es un entero!. Vuelva a intentarlo!')  
            else:
                return value         
    
        


