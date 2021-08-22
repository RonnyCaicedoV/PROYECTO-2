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
    

                      
ejer= Logica()
numeros = (5,25,5,4)
for num in numeros:
  if ejer.perfecto(num) ==num:
    print(num,"Perfecto") 