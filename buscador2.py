class Buscador :
    def __init__(self, datos):
        self.lista=datos
    
    def buscar(self,buscado):
        encontrado= False
        for posi, eleme in enumerate(self.lista):
            if eleme==buscado:
                encontrado= True
                break
        if encontrado: return posi
        else: return -1
                
    
            
da= [2,3,5,7]
bus = Buscador(da)


busca=4
resp= bus.buscar(busca)
if resp !=-1: print("El numero:{} se encuentra en la posicion:[{}] de la lista: {}".format(busca,resp,bus.lista))
else: print("El numero: {} no se encuentra en la lista: {}".format(busca,bus.lista))  
   
