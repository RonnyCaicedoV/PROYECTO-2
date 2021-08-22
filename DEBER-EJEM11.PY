#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros,
# utilizando un bucle controlado por centinela.

class Tarea ():
    def __init__(self):
        pass
    
    def sumprocenti (self):
        sum=0
        prod=1
        num= int(input("Ingrese cualquier numero si desea hacer calculos: "))
        while num >= 0:
            
            num= int(input("Escriba su numero: "))
            if num <=  -1:
                 break
           
            sum= sum+num
            prod= prod*num
            print("El total de la suma es: ",sum)
            print("El total del  producto es: ", prod)
            
            
        if num <=  -1:
         print("Gracias buenas noches")
            
       
        
eje= Tarea()
eje.sumprocenti()