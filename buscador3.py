class Buscador :
    def __init__(self, datos):
        self.lista=datos
    def recorrer_elem(self):
        for eleme in self.lista:
            print(eleme,end=" ")
        print()
        for eleme in self.lista[::-1]:
            print(eleme,end=" ")
        print()
        for contra in enumerate(self.lista):
            print("[{}]={}  ".format(contra,eleme))
        print()
        for contra in range(len(self.lista)-1,-1,-1):
            print("[{}]={}  ".format(contra,self.lista[contra]))
    
    
    def buscar(self,buscado):
        encontrado= False
        for posi, eleme in enumerate(self.lista):
            if eleme==buscado:
                encontrado= True
                break
        if encontrado: return posi
        else: return -1
                
    
            
da= [2,3,1,5,8]
bus = Buscador(da)
   
numerosbuscados= (2,4,6,1)
respuestas = {}
for valor in numerosbuscados:
    resp= bus.buscar(valor)
    if resp !=-1: respuestas[valor]=resp 
print(respuestas)