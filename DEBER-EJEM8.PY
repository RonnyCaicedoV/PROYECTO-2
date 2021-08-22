#Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el 
# resultado.

class Tarea ():
    def __init__(self):
        pass
    def cuadrado (self):
        suma=0
        for i  in range (1,100):
            suma= suma+i*i
        print("La suma de los cuadrados  es: ",suma)
        
eje= Tarea()
eje.cuadrado()
        
    
        