#Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento 
# del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.

class ejem4:
    def __init__(self):
        pass
    
    def Nuevosalario(self):
        sueldo= int(input("Ingrese su sueldo: "))
        if sueldo <= 600:
            sueldofinal= sueldo+sueldo* 0.10
            
        else:  
            sueldofinal=sueldo
        print(" su sueldo final es de: {}".format(sueldofinal))
        
ej4= ejem4()
ej4.Nuevosalario()
