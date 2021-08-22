
from cargo import Cargo

class Empleado:
    secuencia=0
    
    def __init__(self,nom,carg):
        self.codigo=self.generar_Codigo()
        self.nombre=nom 
        self.cargo=carg
        
    def generar_Codigo(self):
        Empleado.Secuencia=Empleado.Secuencia+1
        return Empleado.Secuencia
    
    def mostrar (self):
        print("({})-Nombre:{} ({})-Cargo:{} ".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.descripcion)
        

cargo1 = Cargo("Profesor")  
empl1 = Empleado("Sergio",cargo1)
empl1.mostrar()     