class Logica:
    def __init__(self,datos):
        self.lista=datos
        
    def par (self, numero):
        resi = numero % 2
        return resi
        
    def sumpares (self):
        acu = 0
        for num in self.lista:
            if self.par (num)== 0:
                acu = acu + num
        return acu
        
        
        
        
ejerc = Logica ([2,4,5,7,10])
print(ejerc.sumpares())
        