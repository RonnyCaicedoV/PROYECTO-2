#Aplicar los pasos de la metodología para la solución de un problema para leer
# un número entero N y calcular el resultado de la siguiente serie
#1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. Resolveremos el problema utilizando bucle 
# Repeat controlado por contador y usando banderas.


class Tarea ():
    def __init__(self):
        pass
    
    def calcularserie (self):
      t = 1
      c1 = 1
      cont = 1
      cant2 = 2
      numero=int(input("Digite un numero"))
      while numero<2:
        print("El numero debe ser mayor a 1")
        numero=int(input("intente de nuevo:"))
      while cont<numero:
        if cant2%2==0:
          t=t-(1/(c1+1))
        else:
         t=+(1/(c1+1))
         c1=c1+1
         cant2=cant2+1
         cont=cont+1
        print(t)
        
        
eje = Tarea()        
eje.calcularserie()