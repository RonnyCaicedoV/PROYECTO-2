class Condicion:
    
    def __init__(self,num1,num2):
        self.numero1=num1
        self.numero2=num2
        numero = self.numero1+self.numero2
        self.numero3=numero
    def Condicion(self):
        if self.numero1 == self.numero2:
          print("numero1{} y numero2:{} son iguales".format(self.numero1,self.numero2)) 
        elif  self.numero1 < self.numero3:
          print("Numero1:{} es menor numero3:{}" .format(self.numero1, self.numero3))
        else:
          print("No son para nada iguales")
        print("Final del metodo")
        
         
condi1 = Condicion(12,14)
print(condi1.numero3)
print(condi1.Condicion())

