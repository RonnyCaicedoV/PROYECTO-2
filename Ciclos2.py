class Ciclo:
    def __init__(self,num=15):
        self.numero=num
        
    def usowhile(self):  
            
        caracter=""
        while caracter not in("a","e","i","o","u"):
            caracter = input("Ingrese vocal: ").lower()
            
                
        print("Felicidades el caracter:{} si es una vocal".format(caracter))
    
ciclo1 = Ciclo()

ciclo1.usowhile()