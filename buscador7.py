class Buscador:
    def __init__(self,datos):
        self.lista=datos
      
    def eliminar(self, num):
        enc=False
        for pos,ele in enumerate(self.lista):
            if num == ele:
                enc=True
                break
        if enc==True:
            self.lista= self.lista[0:pos] + self.lista[pos+1:]  
            
            
datos = [5,10,26,30]
num=26
bus= Buscador(datos)
print(bus.lista)
bus.eliminar(num)
print(bus.lista)