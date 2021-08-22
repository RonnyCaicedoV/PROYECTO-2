class Logica:
    def __init__(self):
        pass
    def par (self,numero):
       resi = numero % 2
       return resi
        
ejer= Logica()
#num = numero = int(input("Digite su numero: "))
numeros= [1,2,9,4,5,10]
pares = []
impares= {}
for num in numeros: 
    if ejer.par(num) == 0:
        pares.append(num)
        print(num,"Es par")
    else:
        impares[num]= "Impares"
print(pares) 
print(impares)  