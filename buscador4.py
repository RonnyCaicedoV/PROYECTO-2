class Buscador:
    def __init__(self,datos):
        self.lista=datos
        
    
    def OrdenAscend(self):
        for pos in range(0,len(self.lista)-1):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos] > self.lista[sig]:
                    auxi= self.lista[pos]
                    self.lista [pos]=self.lista[sig]
                    self.lista[sig]= auxi
                    
                    
                    
    def OrdenDescend(self):
        for pos in range(0,len(self.lista)-1):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos] < self.lista[sig]:
                    auxi= self.lista[pos]
                    self.lista [pos]=self.lista[sig]
                    self.lista[sig]= auxi
                    
                    
    
                    
datos= [30,20,25,15]
bus = Buscador(datos)
print(bus.lista)
bus.OrdenAscend()
print(bus.lista)
bus.OrdenDescend()
print(bus.lista)

        