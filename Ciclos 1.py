class Ciclo:
    def __init__(self,num=15):
        self.numero=num
        
    def usowhile(self):
        print("Esta Dentro de la clase",self.numero)  
        
        
        caracter=""
        while caracter not in("a","e","i"):
            caracter = input("Ingrese una vocal: ").lower()
            caracter= caracter.lower()
                
        print("Felicidades el caracter:{} si es una vocal".format(caracter))
    
ciclo1 = Ciclo()
print(" Esta Fuera de la clase",ciclo1.numero)
print(ciclo1.usowhile())
ciclo1.usowhile()