class Logica:
    def __init__(self):
        pass
     
    def perfecto(self,numero):
        acum=0
        for divisor in range (1,numero):
            resi= numero%divisor
            if resi== 0:
                acum= acum+divisor
        return acum
    
    def divisoresNum(self,numero):
        divisores = []
        for divisor in range (1,numero):
            resi= numero%divisor
            if resi== 0:
                divisores.append()
        return divisores

                      
ejer= Logica()
numero = int(input("Digite su numero: "))
print(ejer.divisoresNum(numero))
""" numeros = (5,25,5,4)
for num in numeros:
  if ejer.perfecto(num) ==num:
    print(num,"Perfecto") """
  