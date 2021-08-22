class Buscador :
    def __init__(self, datos):
        self.lista=datos
    def recorrer_elem(self):
        for eleme in self.lista:
            print(eleme,end=" ")
        print("Recorriendo valores")
        print()
        
        for eleme in self.lista[::-1]:
            print(eleme,end=" ")
        print("Recorriendo valores de atras para adelante")
        print()
        
        for contra in enumerate(self.lista):
            print("[{}]={}  ".format(contra,eleme))
        print("Reacorriendo la posicion y valor con enumerate")
        print()
        
        for contra in range(len(self.lista)-1,-1,-1):
            print("[{}]={}  ".format(contra,self.lista[contra]))
        print("Recorriendo posicion y valor con range")
    
                  
    
            
da= [2,4,6,7,9]
bus = Buscador(da)
bus.recorrer_elem()

