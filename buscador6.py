class Buscador:
    def __init__(self,datos):
        self.lista=datos
        
    def ordenarAsce(self):
        for pos in range(0,len(self.lista)-1):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos] > self.lista[sig]:
                    auxi= self.lista[pos]
                    self.lista [pos]=self.lista[sig]
                    self.lista[sig]= auxi
        
    def insertar(self, num):
        self.ordenarAsce()
        auxilist=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                auxilist.append(num)
                break
        self.lista= self.lista[0:pos] + auxilist + self.lista[pos:]  
            
            
datos = [5,10,26,30]
num=22
bus= Buscador(datos)
print(bus.lista)
bus.insertar(num)
print(bus.lista)