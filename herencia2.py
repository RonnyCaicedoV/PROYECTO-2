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
    
    def divisoresNum(self,numero):
        divisores = []
        for divisor in range (1,numero):
            resi= numero%divisor
            if resi== 0:
                divisores.append()
        return divisores
    
    
    
class ejercicio(Logica):
    def __init__(self,numeros,valor):
        super().__init__(numeros)
    
    def suma(self,n1,n2):
        if super().par(n1)==0:
           return (n1+n2)*2
        else:
           return (n1+n2)
    def resta (self,n1,n2):
        return n1-n2
    
    def par (self,numero):
        resi = numero % 2
        if resi == 0:
            print(numero, "El numero es par")
        else:
            print(numero, "Es impar")
ejer = ejercicio([4,5,6],24)
print (ejer.sumpares())
print(ejer.suma(4,7))
