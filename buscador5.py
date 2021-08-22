class Buscador:
    def __init__(self,datos):
        self.lista=datos
        
    def primerelem(self):
        return self.lista[0]
    
    def elementoprimer(self):
        primero= self.lista[0]
        self.lista = self.lista[1:]
        return primero 
    
    def ultimoelem(self):
        return self.lista[-1]
    
    def eliminadoultimo(self):
        ultimo= self.lista[-1]
        self.lista = self.lista[:-1]
        return ultimo
        
      
    

   
datos= [30,20,25,15]
print(datos)
bus = Buscador(datos)
print(bus.primerelem(),bus.lista)


datos= [30,20,25,15]
print(datos)
bus = Buscador(datos)
print(bus.ultimoelem(),bus.lista)